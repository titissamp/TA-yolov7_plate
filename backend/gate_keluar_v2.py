import cv2
import base64
import tkinter as tk
from PIL import Image, ImageTk
from detect_rec_plate_custom import main
import time
import requests,json

def capture_photo():
    # Open default camera
    cap = cv2.VideoCapture(0)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Error opening video capture device")
        return

    # Capture the photo
    ret, frame = cap.read()

    # Release the camera
    cap.release()

    # Check if the photo was captured successfully
    if not ret:
        print("Error capturing photo")
        return

    # Save the photo to disk
    filename = "photo.jpg"
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    cv2.imwrite(filename, frame)
    # Save the photo to a file
    cv2.imwrite("imgs/photo_temp.jpg", frame)
    # Read the image file as bytes
    with open('imgs/photo_temp.jpg', 'rb') as f:
        encoded_image = base64.b64encode(f.read())

    # Set the API endpoint URL
    url = 'http://127.0.0.1:5000/identifikasi_keluar'

    # Set the request headers
    headers = {"Content-Type": "image/jpeg"}
    
    data = {
        'photo': encoded_image.decode('utf-8'),
        'filename': number
    }


    response = requests.post(url, json=data)

    # Send the request
    #response = requests.post(url, data=image_data, headers=headers)
    print(response.text)

# Main loop
while True:
    # Output Voice : Suara "Silahkan Tap Kartu"
    user_input = input("Enter a number (x to exit): ")

    # Exit the program if the user enters 0
    if user_input == "x":
        break

    # Capture a photo if the user enters a number
    try:
        number = (user_input)
        capture_photo()
        time.sleep(2)
    except ValueError:
        # Output Voice : Suara "Silahkan Coba Lagi"
        print("Invalid input, please enter a number or 0 to exit")