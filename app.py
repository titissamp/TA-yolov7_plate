import cv2
import tkinter as tk
from PIL import Image, ImageTk
from detect_rec_plate_custom import main
import argparse
# Initialize the video capture object
cap = cv2.VideoCapture(0)

# Create the GUI window
root = tk.Tk()
root.title("Scan Plat Nomor")
def on_key_press(event):
    number = entry.get()
    capture_photo(number)
# Define a function to capture a photo
def capture_photo(number):
    if len(number) >= 12:
        #Read a frame from the video stream
        ret, frame = cap.read()
        # Convert the frame to RGB format
        # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        # Convert the frame to a PIL ImageTk object
        frame = cv2.flip(frame, 1)
        image = Image.fromarray(frame)
        photo = ImageTk.PhotoImage(image)
        # Display the photo in a label
        label.config(image=photo)
        label.image = photo
        # Save the photo to a file
        cv2.imwrite("imgs/photo2.jpg", frame)
        opt = argparse.Namespace()
        opt.detect_model = 'weights/yolov7-lite-s.pt'
        opt.rec_model = 'weights/plate_rec.pth'
        opt.source = 'imgs/photo2.jpg'
        opt.img_size = 640
        opt.output = 'result'
        opt.kpt_label = 4
        plat_nomor = main(opt)
        text = tk.Text(root)
        text.insert('1.0',f'Plat Nomor: {plat_nomor}')
        text.pack()

#Namespace(detect_model=['weights/yolov7-lite-s.pt'], rec_model='weights/plate_rec.pth', source='imgs', img_size=640, output='result', kpt_label=4)
# Create a label to display the video stream
label = tk.Label(root)
label.pack()
label2 = tk.Label(root, text="Enter a 12 digit number:")
label2.pack()
entry = tk.Entry(root)
entry.pack()
entry.bind('<KeyRelease>', on_key_press)
# Create a button to capture a photo
button = tk.Button(root, text="Capture Photo", command=capture_photo)
button.pack()
# Start the GUI main loop
while True:
    #Read a frame from the video stream
    ret, frame = cap.read()
    #Convert the frame to RGB format
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.flip(frame, 1)
    # Convert the frame to a PIL ImageTk object
    image = Image.fromarray(frame)
    photo = ImageTk.PhotoImage(image)
    # Display the photo in a label
    label.config(image=photo)
    label.image = photo
    # Update the GUI window
    root.update()

class Options:
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)