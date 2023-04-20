from flask import Flask, request, jsonify
# import sys 
import base64
# sys.path.append('D:/TUGASAKHIR/Github/TA-yolov7_plate/YOLOv7/')
from identifikasi_plat import identifikasi_masuk
import cv2
# from identifikasi_plat import identifikasi_keluar
import os
app = Flask(__name__)

@app.route('/identifikasi_masuk', methods=['POST'])
def identifikasi_masuk():
    data = request.get_json()
    photo = data['photo']
    filename = data['filename']
    # Decode base64 encoded image
    image_data = base64.b64decode(photo)
    # Save the image
    with open(f'data_riwayat/image_{filename}.jpg', 'wb') as f:
        f.write(image_data)
    return jsonify({'message': f'Photo {filename}.jpg saved.'})

@app.route('/identifikasi_keluar', methods=['POST'])
def identifikasi_keluar():
    data = request.get_json()
    rfid = data['RFID']
    photo = data['photo']
    return jsonify(identifikasi_masuk(rfid,photo))

if __name__ == '__main__':
    app.run(debug=True)