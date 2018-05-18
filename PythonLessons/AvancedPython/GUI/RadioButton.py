from tkinter import *

root = Tk()

v = IntVar()
v.set(1)

languages = [("Python", 1), ("Perl1", 2), ("C++", 3),("Java", 4),("PHP", 5)]

def ShowChoice():
    print(v.get())
Label(root, text="""Choose your favorite programming language:""",
justify = LEFT, padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, text=txt,
                #Addthese two after typing in the while code)

                #indicatoron = 0,
               # width = 20,
                padx = 20,
                variable = v,
                command=ShowChoice,
                value=val).pack(anchor=W)
mainloop()
