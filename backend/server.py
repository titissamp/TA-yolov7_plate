from flask import Flask, request, jsonify
# import sys 
import base64
# sys.path.append('D:/TUGASAKHIR/Github/TA-yolov7_plate/YOLOv7/')
from postgresql_conn import *
import cv2
from identifikasi_plat import identifikasi_plat_nomor
import os
from datetime import datetime

app = Flask(__name__)
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
    
    # Identifikasi Pelat Nomor
    bukti_masuk = "data_riwayat/image_" + filename + ".jpg"
    pelat = identifikasi_plat_nomor(bukti_masuk)
    if pelat != None:
        # Simpan di PostgreSQL
        id_mhs = add_mhs_masuk(rfid, pelat)
        result = add_riwayat_masuk(bukti_masuk, id_mhs)
        
        return jsonify({'message': result})
    else:
        print("error")
        return jsonify({'error': "error pelat tidak terdeteksi"})

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
    pelat = identifikasi_plat_nomor(bukti_keluar)
    if pelat != None:
        # Cocokkan dengan yang ada di PostgreSQL
        mhs =  get_mhs_data_by_rfid(rfid)
        if mhs != None:
            if mhs[0][1] == pelat:
                status = 1
                id_mhs = update_mhs_keluar(rfid, status)
            else:
                send_alert()
                #Simpan dgn status 2 jika keluar
                status = 2
                id_mhs = update_mhs_keluar(rfid, status)
            result = update_riwayat_keluar(bukti_keluar, id_mhs)
            return jsonify({'message': "Mahasiswa keluar dengan penahanan KTM/KTP"})
        else :
            return jsonify({'error': "Error RFID belum terdaftar masuk"})
    else:
        return jsonify({'error': "Error pelat tidak terdeteksi"})

@app.route('/get_riwayat_parkir', methods=['GET'])
#
# Requirement : Input = - 
#               Output = Record riwayat parkir
# 
def get_riwayat_parkir():
    data = get_all_riwayat_parkir()
    return jsonify({data})

@app.route('/get_gate_status', methods=['GET'])
#
# Requirement : Input = - 
#               Output = Record riwayat parkir
# 
def get_gate_status():
    data = request.get_json()
    gate_id = data['gate_id']
    return jsonify({'gate_id': gate_id})

def send_alert():
    return 1

if __name__ == '__main__':
    app.run(debug=True)