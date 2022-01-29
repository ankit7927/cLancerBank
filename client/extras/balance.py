from tkinter import *
from tkinter import messagebox
import requests, json
from .services import getHeaders
from tkinter.ttk import *


def getBalance(accNO):
    url="http://localhost:8000/balance/get/"+str(accNO)
    res=requests.get(url=url, headers=getHeaders())
    res.json()
    if res.status_code == 200:
        messagebox.showinfo("Balance", "Balance : "+str(json.loads(res.text)["balance"])+" Rs.")
    else:
        messagebox.showerror(str(res.status_code), res.text)



def dipowith(accNO, type):
    root = Toplevel()
    root.title(type+" ammount")
    root.geometry("350x200")
    amountVar=StringVar()

    def working():
        url="http://localhost:8000/balance/"+type
        if amountVar.get() == '':
            messagebox.showwarning("Fields", "all fields are required")
            return

        data={
            "accountNO":int(accNO),
            "ammount":int(amountVar.get())
        }
        res=requests.put(url=url, data=json.dumps(data), headers=getHeaders())
        if res.status_code == 200:
            messagebox.showinfo("Succsfull", f"Amount {type} Succesfully")
            root.destroy()
        else:
            messagebox.showerror(str(res.status_code), res.text)

    Label(root, text="Amount").grid(row=0, column=0, padx=20, pady=10)
    Entry(root, textvariable=amountVar).grid(row=0, column=1, padx=20, pady=5)
    Button(root,text=type, command=working).grid(row=1, column=1, padx=10, pady=8)

    root.mainloop()


def transfer(accNO):
    root = Toplevel()
    root.title("Transfer Ammount")
    root.geometry("350x200")
    accountVar=StringVar()
    amountVar=StringVar()

    def transfering():
        url="http://localhost:8000/balance/transfer"
        if amountVar.get() == '' or accountVar.get()== '':
            messagebox.showwarning("Fields", "all fields are required")
            return

        data={
            "AaccountNO":int(accNO),
            "BaccountNO":int(accountVar.get()),
            "ammount":int(amountVar.get())
        }
        res=requests.put(url=url, data=json.dumps(data), headers=getHeaders())
        if res.status_code == 200:
            messagebox.showinfo("Succsfull", "Amount Transfered Succesfully")
            root.destroy()
        else:
            messagebox.showerror(str(res.status_code), res.text)

    Label(root, text="Amount").grid(row=0, column=0, padx=20, pady=10)
    Entry(root, textvariable=amountVar).grid(row=0, column=1, padx=20, pady=5)

    Label(root, text="Account No.").grid(row=1, column=0, padx=20, pady=10)
    Entry(root, textvariable=accountVar).grid(row=1, column=1, padx=20, pady=5)
    Button(root,text="Transfer", command=transfering).grid(row=2, column=1, padx=10, pady=8)

    root.mainloop()


def transView(tree, transections):
    for item in tree.get_children():
        tree.delete(item)
    for trans in transections:
        tree.insert('', END, values=(trans["type"], trans["ammount"], trans["prieor"]))







