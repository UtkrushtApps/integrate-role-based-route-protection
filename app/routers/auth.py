from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas import Token, UserLogin
from app.services.auth import authenticate_user, create_access_token
from app.dependencies import get_current_user

router = APIRouter()

@router.post('/login', response_model=Token)
def login(user_login: UserLogin):
    # TODO: Implement the login logic, authenticate the user
    # and return an access token if successful
    pass
