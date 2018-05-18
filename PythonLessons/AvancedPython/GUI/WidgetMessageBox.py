#First we will create a message box
from tkinter import *
master = Tk()

whatever_you_do = "Welcome To Advanced Python Course. I love Python!"

msg = Message(master, text = whatever_you_do)

msg.config(bg='white', font=('times',22, 'italic'))

msg.pack()
mainloop()

# Second we will create an image box with Python image

from tkinter import *

canvas_width = 1920
canvas_height = 1080

master = Tk()
canvas = Canvas(master, width = canvas_width, height=canvas_height)
canvas.pack()

img = PhotoImage(file="Small-mario.png")

canvas.create_image(20,20, anchor=NW, image=img)
mainloop()

# We'll want to be able to draw freehand on the canvas by dragging the mouse

from tkinter import *
from tkinter import ttk

lastx, lasty = 0,0

def xy(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x, event.y
def addLine(event):
    global lastx, lasty
    canvas.create_line((lastx, lasty, event.x, event.y))
    lastx, lasty = event.x ,event.y
    
root = Tk()
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

canvas = Canvas(root)
canvas.grid(column=0, row= 0, sticky=(N, W, E, S))
canvas.bind("<Button-1>", xy)
canvas.bind("<B1-Motion>", addLine)
root.mainloop()
