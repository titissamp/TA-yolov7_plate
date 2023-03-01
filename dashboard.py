import cv2
import tkinter as tk
from PIL import Image, ImageTk
#from detect_rec_plate_custom import main
import argparse
# Initialize the video capture object
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 512)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 192)
# Create the GUI window
root = tk.Tk()
root.title("Scan Plat Nomor")
root.geometry("1024x768")
root.resizable(0, 0)
leftbar = tk.Frame(root, width=512, bg='white' , relief='sunken', borderwidth=2)
leftbar.pack(expand=False, fill='both', side='left', anchor='w')
rightbar = tk.Frame(root, width=512, bg='white', relief='sunken', borderwidth=2)
rightbar.pack(expand=False, fill='both', side='right', anchor='e')

title = tk.Label(leftbar, width=45, text="Gate Parking Otomatis\nPoliteknik Negeri Bandung", font=("Arial", 16))
title.pack(anchor="w")
frontLab = tk.Label(rightbar,width=512, text="Kamera Gerbang Masuk", font=("Arial", 16))
frontLab.pack()
frontCam = tk.Label(rightbar, height=260, bg='black', relief='sunken', borderwidth=2) 
frontCam.pack()
backLab = tk.Label(rightbar,width=512, text="Kamera Gerbang Keluar", font=("Arial", 16))
backLab.pack()
backCam = tk.Label(rightbar, height=260, bg='black', relief='sunken', borderwidth=2)  
backCam.pack()

historyLab = tk.Label(rightbar,width=512, text="Last Captured", font=("Arial", 16))
historyLab.pack()

historyCam = tk.Frame(rightbar, width=512, height=400, bg='black', relief='sunken', borderwidth=2) 
historyCam.pack(expand=False, fill='both', side='top', anchor='s')
hLeftBar = tk.Frame(historyCam, width=254, height=200, bg='white', relief='sunken', borderwidth=2) 
hLeftBar.pack(expand=False, fill='both', side='left', anchor='w')
hRightBar = tk.Frame(historyCam, width=254, height=200, bg='white', relief='sunken', borderwidth=2) 
hRightBar.pack(expand=False, fill='both', side='right', anchor='e')

frontHistory = tk.Label(hLeftBar,width=35, text="Kamera Gerbang Keluar", font=("Arial", 8))
frontHistory.pack(expand=False, fill='none', side='top', anchor='n')
hFrontCam = tk.Frame(hLeftBar, width=230, height=200, bg='black', relief='sunken', borderwidth=2) 
hFrontCam.pack(expand=False, fill='none', side='bottom', anchor='s')

backHistory = tk.Label(hRightBar, width=37, text="Kamera Gerbang Masuk", font=("Arial", 8))
backHistory.pack(expand=False, fill='none', side='top', anchor='n')
hLeftCam = tk.Frame(hRightBar, width=240, height=200, bg='black', relief='sunken', borderwidth=2) 
hLeftCam.pack(expand=False, fill='none', side='bottom', anchor='s')
# hideSidebar = tk.Button(sidebar, text ="Hide Basic Tool", font=("Arial", 9, 'bold'))
# hideSidebar.pack(expand=False, fill='both', side='top', anchor='n')

# def on_key_press(event):
#     number = entry.get()
#     capture_photo(number)
# # Define a function to capture a photo
# def capture_photo(number):
#     if len(number) >= 12:
#         #Read a frame from the video stream
#         ret, frame = cap.read()
#         # Convert the frame to RGB format
#         # frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         # Convert the frame to a PIL ImageTk object
#         frame = cv2.flip(frame, 1)
#         image = Image.fromarray(frame)
#         photo = ImageTk.PhotoImage(image)
#         # Display the photo in a label
#         label.config(image=photo)
#         label.image = photo
#         # Save the photo to a file
#         cv2.imwrite("imgs/photo2.jpg", frame)
#         opt = argparse.Namespace()
#         opt.detect_model = 'weights/yolov7-lite-s.pt'
#         opt.rec_model = 'weights/plate_rec.pth'
#         opt.source = 'imgs/photo2.jpg'
#         opt.img_size = 640
#         opt.output = 'result'
#         opt.kpt_label = 4
#         plat_nomor = main(opt)
#         text = tk.Text(root)
#         text.insert('1.0',f'Plat Nomor: {plat_nomor}')
#         text.pack()

# #Namespace(detect_model=['weights/yolov7-lite-s.pt'], rec_model='weights/plate_rec.pth', source='imgs', img_size=640, output='result', kpt_label=4)
# # Create a label to display the video stream
# label = tk.Label(root)
# label.pack()
# label2 = tk.Label(root, text="Enter a 12 digit number:")
# label2.pack()
# entry = tk.Entry(root)
# entry.pack()
# entry.bind('<KeyRelease>', on_key_press)
# # Create a button to capture a photo
# button = tk.Button(root, text="Capture Photo", command=capture_photo)
# button.pack()
# # Start the GUI main loop
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
    frontCam.config(image=photo)
    frontCam.image = photo
    backCam.config(image=photo)
    backCam.image = photo
    # Update the GUI window
    root.update()

 
# class Options:
#     def __init__(self, **kwargs):
#         self.__dict__.update(kwargs)