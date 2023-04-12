import tkinter as tk

def calculate(number):
    if len(number) >= 12:
        # Do something with the input
        print(f"Input received: {number}")
        # Clear the input field
        entry.delete(0, tk.END)

def on_key_press(event):
    number = entry.get()
    calculate(number)

root = tk.Tk()
root.title("12 Digit Input")
root.geometry("300x100")

label = tk.Label(root, text="Enter a 12 digit number:")
label.pack()

entry = tk.Entry(root)
entry.pack()

entry.bind('<KeyRelease>', on_key_press)

root.mainloop()
