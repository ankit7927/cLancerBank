from fastapi import APIRouter, Body, HTTPException
from database.schemas import createUserSchema, updateUserSchema
from database.actions import getDatabase, saveDatabase

router = APIRouter()


users=getDatabase("users")


@router.get("/user/get")
def get_users():
    return {"users":users}


@router.post("/user/create")
def create_user(body:createUserSchema):       
    body.accountNO=len(users)+1
    users.append(body.dict())
    saveDatabase(users, "users")
    return {"info":"user created"}


@router.put("/user/update/{accNO}")
def update_user(accNO:int, body:updateUserSchema):
    for user in users:
        if user['accountNO']==accNO:
            user['name']=body.name
            user['email']=body.email
            saveDatabase(users, "users")
            return {"info":"user updated succ"}

    raise HTTPException(status_code=404, detail="user not found, failed to update")


@router.delete("/user/remove/{accNO}")
def delete_user(accNO:int):
    for user in users:
        if user['accountNO']==accNO:
            users.remove(user)
            saveDatabase(users, "users")
            return {"info":"user removed succ"}
    raise HTTPException(status_code=404, detail="user not found, failed to remove")


@router.get("/user/get/{accNO}")
def get_user(accNO:int):
    for user in users:
        if int(user['accountNO'])==accNO:
            return user

    raise HTTPException(status_code=404, detail="user not found, wrong account no")


