import cv2
import base64
import tkinter as tk
from PIL import Image, ImageTk
from detect_rec_plate_custom import main
import time
import requests,json
import cloudinary
import cloudinary.uploader
import io
import os 

def upload_file(filename):

  cloudinary.config(
    cloud_name = "jtk",
    api_key = "256473613645129",
    api_secret = "608g68rUKA13x6RFA3r5zfqVv5k"
  )
  image = Image.open(filename)
  with io.BytesIO() as output:
        image.save(output, format='JPEG')
        image_data = output.getvalue()
  response = cloudinary.uploader.upload(image_data)
  return response['url']

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
    
    # Save the photo to a file
    cv2.imwrite(filename, frame)

    # Read the image file as bytes
    with open(filename, 'rb') as f:
        encoded_image = base64.b64encode(f.read())

    # Set the API endpoint URL
    url = 'http://127.0.0.1:6009/identifikasi_masuk'

    # Set the request headers
    headers = {"Content-Type": "image/jpeg"}
    
    data = {
        'photo': encoded_image.decode('utf-8'),
        'filename': number
    }


    response = requests.post(url, json=data)
    response = json.loads(response.text)
    # Send the request
    #response = requests.post(url, data=image_data, headers=headers)
    print(response)
    if(response['code'] == 200):
        #print(response['user_id'])
        #print("ini urlnya: " + upload_file(filename))
        data_bukti = {
            'bukti_masuk' : upload_file(filename),
            'user_id' : response['user_id']
        }
        url_bukti = 'http://127.0.0.1:6009/update_bukti_masuk'
        response = requests.post(url_bukti, json=data_bukti)
    
    os.remove(filename)

# Main loop
while True:
    # Get input from the user
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
        print("Invalid input, please enter a number or 0 to exit")

# RFID test = 12345678901

