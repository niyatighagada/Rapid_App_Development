import tkinter as tk
import os
import sys
import tkinter.font as tkFont
from tkinter import messagebox
from PIL import Image, ImageTk


def startattendace():
    os.system('python3 videoTester.py')

def close_window():
    root.destroy()

root = tk.Tk()
root.geometry("500x500")


background_image = tk.PhotoImage(file='bus2.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
root.configure(bg='yellow')
fontStyle = tkFont.Font(family="Lucida Grande", size=20)
label = tk.Label(root, text="FALCON ATTENDANCE", width=200, font=fontStyle)
label.pack(padx=20, pady=20)



B1=tk.Button(root,text="start attendance system",command= startattendace, font=fontStyle)
#B2=tk.Button(root,text="stop attendance system",command= close_window)
B1.pack()
#B2.pack()
root.mainloop()