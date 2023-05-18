from flask import Flask, request, jsonify
# import sys 
import base64
# sys.path.append('D:/TUGASAKHIR/Github/TA-yolov7_plate/YOLOv7/')
from postgresql_conn import *
import cv2
from identifikasi_plat import identifikasi_plat_nomor
import os
from datetime import datetime
# import cloudinary
# import cloudinary.uploader
from PIL import Image
import io

app = Flask(__name__)
# cloudinary.config(
#   cloud_name = "jtk",
#   api_key = "256473613645129",
#   api_secret = "608g68rUKA13x6RFA3r5zfqVv5k"
# )


@app.route('/identifikasi_masuk', methods=['POST'])
#
# Requirement : Input = RFID & Gambar. => Identifikasi pelat nomor => Simpan di PostgreSQL
#
def identifikasi_masuk():
    # Input RFID dan Gambar
    data = request.get_json()
    photo = data['photo']
    rfid = data['filename']
    now = datetime.now() 
    filename = rfid + now.strftime("-%H-%M-%S")
    # Decode base64 encoded image
    image_data = base64.b64decode(photo)
    # Save the image
    with open(f'data_riwayat/image_{filename}.jpg', 'wb') as f:
        f.write(image_data)
    bukti_masuk = "data_riwayat/image_" + filename + ".jpg"
    # Cek RFID sedang digunakan/tidak
    mhs =  get_mhs_data_by_rfid(rfid)
    #print("MAhasiswa:")
    #print(mhs)
    if mhs == None:
        # Jika rfid tdk digunakan maka lanjut cek pelat
        # Identifikasi Pelat Nomor
        pelat = identifikasi_plat_nomor(bukti_masuk)        
        if pelat != None:
            # Pelat telah ada
            is_pelat = get_mhs_data_by_pelat(pelat)
            if is_pelat == None:
                id_mhs = add_mhs_masuk(rfid, pelat)
                result = add_riwayat_masuk(bukti_masuk, id_mhs)
                code = 200
            else:
                result = "Pelat telah terdaftar"
                code = 500
        else:
            # Pelat tidak terdeteksi
            os.remove(bukti_masuk)
            code = 504
            result = "error pelat tidak terdeteksi"
    else:
        os.remove(bukti_masuk)
        code = 501
        result = "RFID telah dipakai"
    return jsonify({'message': result, 'code' : code})

@app.route('/identifikasi_keluar', methods=['POST'])
#
# Requirement : Input = RFID & Gambar. => Identifikasi pelat nomor => Cocokkan dengan yang ada di PostgreSQL
#
def identifikasi_keluar():
    # Input RFID dan Gambar
    data = request.get_json()
    photo = data['photo']
    rfid = data['filename']
    now = datetime.now() 
    filename = rfid + now.strftime("-%H-%M-%S")
    # Decode base64 encoded image
    image_data = base64.b64decode(photo)
    # Save the image
    with open(f'data_riwayat/image_{filename}.jpg', 'wb') as f:
        f.write(image_data)
    
    # Identifikasi Pelat Nomor
    bukti_keluar = "data_riwayat/image_" + filename + ".jpg"
    mhs =  get_mhs_data_by_rfid(rfid)
    if mhs != None:
        # Jika ada mhs di database dengan RFID tsb
        pelat = identifikasi_plat_nomor(bukti_keluar)
        if pelat != None:
            # Kalo plat terdeteksi
            print(mhs[0][2])
            if mhs[0][2] == pelat:
                # Kalo pelat sama
                status = 1
                id_mhs = update_mhs_keluar(rfid, status)
                code = 200
                result = update_riwayat_keluar(bukti_keluar, id_mhs)
            else:
                # Kalo pelat beda
                send_alert()
                
                #Simpan dgn status 2 jika pelat berbeda
                status = 2
                id_mhs = update_mhs_keluar(rfid, status)
                os.remove(bukti_keluar)
                code = 501
                result = "Pelat nomor berbeda"
            
            #return jsonify({'message': result, 'code' : code})
        else :
            # Pelat tidak terdeteksi
            os.remove(bukti_keluar)
            result = "Error pelat tidak terdeteksi"
            code = 504
    else:
        # Jika tdk ada mhs dengan RFID tersebut
        os.remove(bukti_keluar)
        code = 501
        result = "RFID belum terdaftar"
    return jsonify({'message': result, 'code' : code})

@app.route('/get_riwayat_parkir', methods=['GET'])
#
# Requirement : Input = - 
#               Output = Record riwayat parkir
# 
def get_riwayat_parkir():
    data = get_all_riwayat_parkir()
    return jsonify({data})

@app.route('/get_riwayat_count', methods=['GET'])
#
# Requirement : Input = - 
#               Output = Record riwayat parkir
# 
def get_riwayat_count():
    data = get_jml_parkir()
    return jsonify({'data': data})

def send_alert():
    return 1


if __name__ == '__main__':
    app.run(debug=True)