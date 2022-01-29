from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from .token import decodeTOKEN


class SecureRoute(HTTPBearer):
    def __init__(self, auto_error: bool = True):
        super(SecureRoute, self).__init__(auto_error=auto_error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(SecureRoute, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                print("invalid auth scheme")
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            if not self.verify_jwt(credentials.credentials):
                print("invalid token")
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            return credentials.credentials
        else:
            print("invalid auth code 403")
            raise HTTPException(status_code=403, detail="Invalid authorization code.")


    def verify_jwt(self, jwtoken) -> bool:
        isTokenValid: bool = False

        try:
            payload = decodeTOKEN(jwtoken)
        except:
            payload = None
        if payload:
            isTokenValid = True
        return isTokenValid


def verify_token(req:Request):
    token=req.headers["Authorization"]
    if decodeTOKEN(token):
        return True
    raise HTTPException(status_code=404, details="not authro")