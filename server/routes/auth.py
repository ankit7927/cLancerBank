from fastapi import APIRouter, Body, HTTPException
from database.schemas import signupSchema, signinSchema
from database.actions import getDatabase, saveDatabase
from security.token import signTOKEN
router = APIRouter()

admins=getDatabase("admins")

@router.post("/auth/signup")
def signup(body:signupSchema = Body(default=None)):
    for admin in admins:
        if admin['uname']==body.uname:
            raise HTTPException(status_code=400, detail="user alredy existsss")
    id=len(admins)+1
    body.id=id
    admins.append(body.dict())
    saveDatabase(admins, "admins")
    token=signTOKEN(str(id))
    return token


@router.post("/auth/signin")
def signup(body:signinSchema):

    for admin in admins:
        if admin['uname']==body.uname and admin['pword']==body.pword:
            #return {"admin":admin["uname"]}
            return signTOKEN(str(admin["id"]))
    raise HTTPException(status_code=404, detail="user doen not exists")


