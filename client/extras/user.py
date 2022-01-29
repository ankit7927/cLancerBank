from tkinter import *
from tkinter import messagebox
from tkinter.messagebox import askyesno
from tkinter.ttk import Treeview

import requests, json
from .services import getHeaders

def create_update(user={}, type="create"):

    root=Toplevel()
    namevar=StringVar()
    emailvar=StringVar()

    if type=="update":
        
        namevar.set(user["name"])
        emailvar.set(user["email"])

    root.title("create user")
    root.geometry("350x200")
    root.resizable(0,0)
        
    def creating_updating():
        
        if namevar.get() == '' or emailvar.get() == '':
            messagebox.showwarning("Fields", "All Fields Are Required")
            return
        if type=="update":
            url="http://localhost:8000/user/update/"+str(user["accountNO"])

            update={
                "name":namevar.get(),
                "email":emailvar.get()
            }
            res=requests.put(url=url, data=json.dumps(update), headers=getHeaders())
        else:
            url="http://localhost:8000/user/create"
            create={
                "name":namevar.get(),
                "email":emailvar.get(),
            }
            res=requests.post(url=url, data=json.dumps(create), headers=getHeaders())
        
        if res.status_code == 200:
            messagebox.showinfo("Succsfull", f"User {type} Succesfully")
            root.destroy()
        else:
            messagebox.showerror(str(res.status_code), res.text)

    Label(root, text="Name").grid(row=0, column=0, padx=20, pady=10)
    Entry(root, textvariable=namevar).grid(row=0, column=1, padx=20, pady=5)
    Label(root, text="Email").grid(row=1, column=0, padx=20, pady=10)
    Entry(root, textvariable=emailvar).grid(row=1, column=1, padx=20, pady=5)
    Button(root,text="Create", command=creating_updating).grid(row=2, column=1, padx=10, pady=8)
    
    root.mainloop()

def remove_usr(accNO):

    def remove(accNO):
        url="http://localhost:8000/user/remove/"+str(accNO)
        res=requests.delete(url=url, headers=getHeaders())
        if res.status_code == 200:
            messagebox.showinfo("Succsfull", "User Removed Succesfully")
        else:
            messagebox.showerror(str(res.status_code), res.text)

    ans = askyesno(title="Remove", message="Are You Sure To Remove\nUser With Account No. " + str(accNO))

    if ans:
        remove(accNO)





def getAllUsers():
    url="http://localhost:8000/user/get"
    res=requests.get(url=url, headers=getHeaders())

    if not res.status_code == 200:
        messagebox.showerror(str(res.status_code), str(res.text))
        return

    allUser=json.loads(res.text)["users"]
    if allUser==[]:
        messagebox.showinfo("Information","No Customers At This Time")
        return

    root = Toplevel()
    root.title("All User")
    root.resizable(0,0)

    tree = Treeview(root, show='headings')
    tree.pack(side=LEFT, expand=1, fill=BOTH)

    scroll = Scrollbar(root, orient=VERTICAL, command=tree.yview)
    scroll.pack(side=RIGHT, fill=Y)

    tree.configure(yscrollcommand=scroll.set)
    tree["columns"] = ('1', '2', '3')

    tree.column("1", width=100, minwidth=50, anchor=CENTER)
    tree.column("2", width=100, minwidth=50, anchor=CENTER)
    tree.column("3", width=100, minwidth=50, anchor=CENTER)

    tree.heading("1", text="Account No.")
    tree.heading("2", text="Name")
    tree.heading("3", text="Email")

    for user in allUser:
        tree.insert('', END, values=(user["accountNO"], user["name"], user["email"]))

    root.mainloop()


def allDetails(accNO):
    url="http://localhost:8000/user/get/"+str(accNO)
    res=requests.get(url=url, headers=getHeaders())

    if res.status_code == 200:
        detail=json.loads(res.text)
    else:
        messagebox.showerror(str(res.status_code), res.text)

    root=Toplevel()
    root.title("All Details")

    root.resizable(0,0)

    temp=["name", "email", "accountNO", "balance"]
    for inx, x in enumerate(temp):
        Label(root, text=temp[inx]+" : ", width=20).grid(row=inx, column=0)
        Label(root, text=detail[x], width=20).grid(row=inx, column=1)
    
    root.mainloop()




