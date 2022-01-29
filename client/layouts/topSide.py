
from tkinter import *
from extras.user import create

def topPanel(root):

    b1=Button(root, text="new custome", command=create).grid(row=0, column=0)#.place(anchor=NW)
    b2=Button(root, text="logout").grid(row=0, column=1)#.place(anchor=NE)
    