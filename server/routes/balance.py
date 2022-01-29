from fastapi import APIRouter, Body, HTTPException
from database.schemas import createUserSchema, balanceSchema, AtoBtransferSchema
from database.actions import getDatabase, saveDatabase


users=getDatabase("users")

router = APIRouter()


@router.get("/balance/get/{accNO}")
def get_balance(accNO:int):

    for user in users:
        if user["accountNO"]==accNO:

            return {"balance":user["balance"]}
    raise HTTPException(status_code=404, detail="user not found")


@router.put("/balance/deposit")
def deposit(body:balanceSchema):
    for user in users:
        if user["accountNO"]==body.accountNO:
            print("user found")
            currBal=user['balance'] + body.ammount
            user['balance']=currBal
            trans={
                "type":"credit",
                "ammount":body.ammount,
                "prieor":"branch"
            }
            user["transections"].insert(0, trans)
            saveDatabase(users, "users")
            return {"info":"deposited"}

    raise HTTPException(status_code=404, detail="failed to deposit")


@router.put("/balance/withdraw")
def deposit(body:balanceSchema):
    for user in users:
        if user['accountNO']==body.accountNO:
            if user['balance'] >= body.ammount:
                currBal=user['balance'] - body.ammount
                user['balance']=currBal
                trans={
                    "type":"debit",
                    "ammount":body.ammount,
                    "prieor":"branch"
                }
                user["transections"].insert(0, trans)
                saveDatabase(users, "users")
                return {"info":"withdrawed"}
            raise HTTPException(status_code=404, detail="not enought balance")

    raise HTTPException(status_code=404, detail="failed to withdraw")



@router.put("/balance/transfer")
def transfer(body:AtoBtransferSchema):
    Aaccount=body.AaccountNO
    Baccount=body.BaccountNO
    if Aaccount==Baccount:
        raise HTTPException(status_code=404, detail="account no. should not be same")
    userAccounts=[]
    for user in users:
        userAccounts.append(user['accountNO'])

    if Aaccount in userAccounts and Baccount in userAccounts:
        for user in users:
            if user['accountNO']==Aaccount:
                if user['balance'] >= body.ammount:
                    currBal=user['balance'] - body.ammount
                    user['balance']=currBal
                    print('ammount subtracted')
                    Atrans={
                        "type":"debit",
                        "ammount":body.ammount,
                        "prieor":Baccount
                    }
                    user["transections"].insert(0, Atrans)

                    for user in users:
                        if user['accountNO']==Baccount:
                            currBal=user['balance'] + body.ammount
                            user['balance']=currBal
                            print("ammount added")
                            Btrans={
                                "type":"credit",
                                "ammount":body.ammount,
                                "prieor":Aaccount
                            }
                            user["transections"].insert(0, Btrans)
                            saveDatabase(users, "users")
                            return {"info":"transfered"}    

                raise HTTPException(status_code=404, detail="not enought ammount")

    raise HTTPException(status_code=404, detail="wrong account no.")

    
@router.get("/balance/trans/{accNO}")
def get_trans(accNO:int):
    for user in users:
        if user['accountNO']==accNO:
            return user["transections"]
    
    raise HTTPException(status_code=404, detail="user not found")
