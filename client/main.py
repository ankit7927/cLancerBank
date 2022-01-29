import os, requests, json
from tkinter import *
from tkinter import messagebox
from layouts.leftSide import leftPanel
from layouts.rightSide import rightPanel
from extras.services import setToken



root = Tk()
root.title("Code Lancer Bank")
root.geometry('400x300+100+70')
root.resizable(0,0)

username = StringVar()
password = StringVar()

def main_window():
    authFrame.pack_forget()
    infoFrame.pack_forget()

    root.geometry('900x600')

    leftFrame = LabelFrame(root, text="Quick Help")
    rightFrame = LabelFrame(root, text="Account Stuffs")

    leftFrame.pack(side=LEFT, fill=BOTH, padx=5, pady=5)
    leftPanel(leftFrame)

    rightFrame.pack(fill=BOTH, padx=5, pady=5)
    rightPanel(rightFrame)


def check_creadentials():
    if username.get()=="" and password.get()=="":
        messagebox.showerror("Error", "Both Fields Required")
        return
        
    url="http://localhost:8000/auth/signin"
    data={
        "uname":username.get(),
        "pword":password.get()
    }
    res=requests.post(url=url, data=json.dumps(data))
    if res.status_code == 200:
        if not setToken(str(res.text)):
            messagebox.showerror("Error", "Unable To Save Token")
            return
        main_window()
    else:
        messagebox.showerror("Error", res.text)





authFrame = LabelFrame(root, text="Login Here")
authFrame.pack(side=TOP, pady=10, padx=20, fill=BOTH)

Label(authFrame, text="Username", width=10).grid(row=0, column=0,padx=10, pady=8)
uname = Entry(authFrame, textvariable=username, width= 25).grid(row=0, column=1)
Label(authFrame, text="Password", width=10).grid(row=1, column=0,padx=10, pady=8)
pword = Entry(authFrame, textvariable=password, width= 25).grid(row=1, column=1)

login_button=Button(authFrame,text="Login", command=check_creadentials, width=20).grid(row=2, padx=10, pady=8, columnspan=2)


infoFrame = LabelFrame(root, text="Information")
infoFrame.pack(side=TOP, pady=10, padx=20, fill=BOTH)
Label(infoFrame, text="Wellcome To My Bank").grid(padx=10, pady=10, row=0, column=0)

file = os.path.exists("bin/token.txt")
if file:
    main_window()

root.mainloop()
