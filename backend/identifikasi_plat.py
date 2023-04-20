import cv2
import tkinter as tk
from PIL import Image, ImageTk
from detect_rec_plate_custom import main
import argparse, pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["gateparking"]
data_mahasiswa = db["data_mahasiswa"]

# Query
postgreSQL_select_Query = "select * from publisher"

# Define a function to capture a photo
def identifikasi_masuk(number, photo):
    opt = argparse.Namespace()
    opt.detect_model = 'weights/yolov7-lite-s.pt'
    opt.rec_model = 'weights/plate_rec.pth'
    opt.source = photo
    opt.img_size = 640
    opt.output = 'result'
    opt.kpt_label = 4
    plat_nomor = main(opt)
    doc = data_mahasiswa.find_one({"$and": [{"rfid": number}, {"plat_nomor": plat_nomor}]})
    if doc:
        print(f"RFID {number} and plat nomor {plat_nomor} are associated with NIM {doc['nim']}")
        return f"RFID {number} and plat nomor {plat_nomor} are associated with NIM {doc['nim']}"
    else:
        print(f"No document found with RFID {number} and plat nomor {plat_nomor}")
        return (f"No document found with RFID {number} and plat nomor {plat_nomor}")

class Options:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)