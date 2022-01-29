import json, os, sys
from tkinter.messagebox import askyesno
from tkinter import  messagebox


def getToken():
    file = open("bin/token.txt", "r")
    return file.read()

def setToken(token):
    try:
        file=open("bin/token.txt", "w")
        file.write(token)
        return True
    except:
        return False

def getHeaders():
    headers={
            "accept":"application/json",
            "Authorization":"Bearer "+json.loads(getToken())["token"]
        }
    return headers

def logout():
    ans=askyesno(title="Logout", message="Are You Sure To Logout ?\nSystem Will Closed")
    if ans:
        try:
            os.remove("bin/token.txt")
            sys.exit()
        except Exception as e:
            print(e)
            messagebox.showerror(title="Error", message="Failed To Exit")
            return
    return
