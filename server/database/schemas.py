from pydantic import BaseModel, Field
from typing import Optional

# admin auth schema
class signupSchema(BaseModel):
    id:Optional[int]=Field(default=0)
    uname:str
    pword:str


class signinSchema(BaseModel):
    uname:str
    pword:str


class createUserSchema(BaseModel):
    name:str
    email:str
    accountNO:Optional[int]=Field(default=0)
    balance:Optional[int]=Field(default=0)
    transections:Optional[list]=Field(default=[])

class updateUserSchema(BaseModel):
    name:str
    email:str


class balanceSchema(BaseModel):
    accountNO:int
    ammount:int


class AtoBtransferSchema(BaseModel):
    AaccountNO:int
    BaccountNO:int
    ammount:int

