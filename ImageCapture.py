# Imports
from PIL import Image, ImageTk
import tkinter as tk
import cv2

# Save Function
def save(num):
    global prevImg

    prevImg.save(f'image{num}.png')

# Get Video
cap = cv2.VideoCapture(0)
_, frame = cap.read()
 
# Setup Main Window
mainWindow = tk.Tk(screenName = "Camera Capture")
mainWindow.resizable(width = False, height = False)
mainWindow.bind('<Escape>', lambda e: mainWindow.quit())
lmain = tk.Label(mainWindow, compound = tk.CENTER, anchor = tk.CENTER, relief = tk.RAISED)

# Attach Buttons to Functions
button1 = tk.Button(mainWindow, text = "1", command = lambda:save(1))
button2 = tk.Button(mainWindow, text = "2", command = lambda:save(2))
button3 = tk.Button(mainWindow, text = "3", command = lambda:save(3))
button4 = tk.Button(mainWindow, text = "4", command = lambda:save(4))
button5 = tk.Button(mainWindow, text = "5", command = lambda:save(5))
button6 = tk.Button(mainWindow, text = "6", command = lambda:save(6))
button7 = tk.Button(mainWindow, text = "7", command = lambda:save(7))
button8 = tk.Button(mainWindow, text = "8", command = lambda:save(8))

lmain.pack()

# Place Buttons
button1.place(bordermode = tk.INSIDE, relx = 0.35, rely = 0.75, anchor = tk.CENTER, width = 50, height = 50)
button2.place(bordermode = tk.INSIDE, relx = 0.45, rely = 0.75, anchor = tk.CENTER, width = 50, height = 50)
button3.place(bordermode = tk.INSIDE, relx = 0.55, rely = 0.75, anchor = tk.CENTER, width = 50, height = 50)
button4.place(bordermode = tk.INSIDE, relx = 0.65, rely = 0.75, anchor = tk.CENTER, width = 50, height = 50)
button5.place(bordermode = tk.INSIDE, relx = 0.35, rely = 0.9, anchor = tk.CENTER, width = 50, height = 50)
button6.place(bordermode = tk.INSIDE, relx = 0.45, rely = 0.9, anchor = tk.CENTER, width = 50, height = 50)
button7.place(bordermode = tk.INSIDE, relx = 0.55, rely = 0.9, anchor = tk.CENTER, width = 50, height = 50)
button8.place(bordermode = tk.INSIDE, relx = 0.65, rely = 0.9, anchor = tk.CENTER, width = 50, height = 50)

# Show Frames to Capture
def show_frame():
    global cancel, prevImg
 
    _, frame = cap.read()
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
 
    prevImg = Image.fromarray(cv2image)
    imgtk = ImageTk.PhotoImage(image = prevImg)
    lmain.imgtk = imgtk
    lmain.configure(image = imgtk)
    lmain.after(10, show_frame)

# Run
show_frame()
mainWindow.mainloop()