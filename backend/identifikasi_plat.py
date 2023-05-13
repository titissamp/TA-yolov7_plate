import cv2
import tkinter as tk
from PIL import Image, ImageTk
from detect_rec_plate_custom import main
import argparse

# Define a function to capture a photo
def identifikasi_plat_nomor(photo):
    try:
        opt = argparse.Namespace()
        opt.detect_model = 'weights/yolov7-lite-s.pt'
        opt.rec_model = 'weights/plate_rec.pth'
        opt.source = photo
        opt.img_size = 640
        opt.output = 'result'
        opt.kpt_label = 4
        plat_nomor = main(opt)
        if plat_nomor:
            return plat_nomor
        else:
            return None
    except (Exception) as error:
        print(" Gadapet bang no platnya ")
        return None

class Options:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)