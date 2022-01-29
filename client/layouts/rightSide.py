import tkinter, requests, json
from tkinter.ttk import *
from tkinter import messagebox
from tkinter import *
from extras.balance import dipowith, getBalance, transfer, transView
from extras.services import getHeaders
from extras.user import create_update, allDetails, remove_usr


class User():
    user = {}
    def setUser(self, data):
        self.user=data

    def getUser(self):
        return self.user



def rightPanel(root):
    topFrame=Frame(root, pady=10,padx=10)
    user=User()
    accountNO=StringVar()
    name=StringVar()
    email=StringVar()

    def searchUser():
        if accountNO.get()=="":
            messagebox.showerror("Required", "Account Number Should Not Be Empty")
            return

        url="http://localhost:8000/user/get/"+str(accountNO.get())
        res=requests.get(url=url, headers=getHeaders())

        if res.status_code == 200:
            user.setUser(json.loads(res.text))

            name.set(user.getUser()['name'])
            email.set(user.getUser()['email'])
            #print(user.getUser()["transections"])
            detailFrame.pack(side=TOP, fill=BOTH, padx=15, pady=10)
            middelFrame.pack(side=TOP, fill=BOTH, padx=15, pady=10)
            bottomFrame.pack(side=TOP, fill=BOTH, padx=15, pady=5)
            transView(tree, user.getUser()["transections"])
            
        else:
            messagebox.showerror(str(res.status_code), res.text)

    def clearUser():
        user.setUser({})
        accountNO.set("")
        name.set("")
        email.set("")
        detailFrame.pack_forget()
        middelFrame.pack_forget()
        bottomFrame.pack_forget()



    topFrame.pack(side=TOP, fill=BOTH)
    Label(topFrame, text="Enter Account No ").grid(row=0, column=0, padx=20)
    accountNO_box=Entry(topFrame, textvariable=accountNO).grid(row=0, column=1)
    search_button=Button(topFrame, text="Search",command=searchUser).grid(row=0, column=2, padx=15, pady=5)
    clear_button=Button(topFrame, text="Clear",command=clearUser).grid(row=0, column=3, padx=15, pady=5)


    detailFrame=LabelFrame(root, pady=8,padx=5, text="Customer Details")
    Label(detailFrame, textvariable=name).grid(row=0, column=0, padx=20)
    Label(detailFrame, textvariable=email).grid(row=0, column=1, padx=20)
    Button(detailFrame, text="Show Details", command=lambda: allDetails(accountNO.get())).grid(row=0, column=2, padx=20)
    Button(detailFrame, text="Update Details", command=lambda: create_update(user.getUser(), "update")).grid(row=0, column=3, padx=20)
    Button(detailFrame, text="Remove User", command=lambda: remove_usr(user.getUser()["accountNO"])).grid(row=0, column=4, padx=20)


    middelFrame=LabelFrame(root, pady=8,padx=5, text="Actions")
    balance_button=Button(middelFrame, text="Check Balance", command=lambda: getBalance(accountNO.get())).grid(row=0, column=0, padx=20)
    deposit_button=Button(middelFrame, text="Deposit", command=lambda: dipowith(accountNO.get(), "deposit")).grid(row=0, column=1, padx=20)
    withdraw_button=Button(middelFrame, text="Withdraw", command=lambda: dipowith(accountNO.get(), "withdraw")).grid(row=0, column=2, padx=20)
    transfer_button=Button(middelFrame, text="Transfer", command=lambda: transfer(accountNO.get())).grid(row=0, column=3, padx=20)



    bottomFrame=LabelFrame(root, pady=8,padx=5, text="Transections")

    tree = Treeview(bottomFrame, show='headings')
    tree.pack(side=LEFT, expand=1, fill=BOTH)

    scroll = Scrollbar(bottomFrame, orient=VERTICAL, command=tree.yview)
    scroll.pack(side=RIGHT, fill=Y)

    tree.configure(yscrollcommand=scroll.set)

    tree["columns"] = ('1', '2', '3')

    tree.column("1", width=100, minwidth=50, anchor=CENTER)
    tree.column("2", width=100, minwidth=50, anchor=CENTER)
    tree.column("3", width=100, minwidth=50, anchor=CENTER)

    tree.heading("1", text="Type")
    tree.heading("2", text="Amount")
    tree.heading("3", text="Prieor")







