from fastapi import FastAPI, Depends
from routes import auth, user, balance
from security.authenticate import SecureRoute, verify_token
app = FastAPI()

app.include_router(auth.router, tags=["auth"])

app.include_router(user.router, tags=["user"], dependencies=[Depends(SecureRoute())])

app.include_router(balance.router, tags=["balance"], dependencies=[Depends(SecureRoute())])

#, dependencies=[Depends(SecureRoute())]
