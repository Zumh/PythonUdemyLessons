# This program create a button
'''
import tkinter
from tkinter import ttk
root = tkinter.Tk()

style = ttk.Style()

style.map("C.TButton",
          foreground=[('pressed','red'), ('active','blue')],
          background=[('pressed','!disabled', 'black'), ('active','white')]
            
          )

colored_btn = ttk.Button(text="Click Me!", style="C.TButton").pack()

root.mainloop()
root.mainloop()
'''

from tkinter import *
canvas_width = 100
canvas_height= 50

class App:
    def __init__(self, master, width=canvas_width, height=canvas_height):
        frame = Frame(master, width=canvas_width, height=canvas_height)

        frame.pack()
        self.button = Button(frame, text="Close", fg="red", command=frame.quit)
        self.button.pack(side=LEFT)
        self.slogan = Button(frame, text="Click Me!", fg = "blue", command=self.write_slogan)

        self.slogan.pack(side=LEFT)
        self.button.config(height = 2, width = 20)
        self.slogan.config(height = 2, width = 20)

    def write_slogan(self):
        print("Welcometo Python Advanced Programming")

root = Tk()
root.title("Hello World")
app = App(root)
root.mainloop()

# this code is for the timer

import tkinter as tk
counter = 0
def counter_label(label):
    counter = 0
    def count():
        global counter
        counter += 1
        label.config(text=str(counter))
        label.after(100, count)
    count()

root = tk.Tk()
root.title("Conting Seconds")
label = tk.Label(root, fg="dark green")
label.pack()
counter_label(label)
button = tk.Button(root, text='Stop', width=55, command=root.destroy)
button.pack()
root.mainloop()



