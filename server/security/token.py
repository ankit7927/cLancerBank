import jwt



secret="mySECREAT"
algo="HS256"

def token_res(token):
    return {
        "token":token
    }

def signTOKEN(userID:str):
    payload={
        "userID":userID,
    }
    token=jwt.encode(payload, secret, algorithm=algo)
    return token_res(token)

def decodeTOKEN(token:str):

    try:
        decoded=jwt.decode(token, secret, algorithms=algo)
        return decoded
    except:
        return None