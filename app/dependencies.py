from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

# TODO: Implement the token url and user validation logic here
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(token: str = Depends(oauth2_scheme)):
    # TODO: Implement the logic to decode and validate JWT token
    # and return current user if valid, raise HTTPException if not valid
    pass
