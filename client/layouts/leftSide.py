from tkinter import *
from extras.services import logout
from extras.user import create_update, getAllUsers



def leftPanel(root):
    Label(root, text="wellcome to my bank", pady=20).grid(row=0, column=0)
    b1=Button(root, text="New Customer", command=create_update, width=15).grid(row=1, column=0, pady=5, padx=10)
    b3=Button(root, text="All Customer", command=getAllUsers, width=15).grid(row=2, column=0, pady=5, padx=10)
    b2=Button(root, text="Admin Logout", width=15, command=logout).grid(row=3, column=0, pady=5, padx=10)




    