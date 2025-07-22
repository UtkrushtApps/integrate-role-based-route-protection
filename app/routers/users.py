from fastapi import APIRouter, Depends
from app.dependencies import get_current_user

router = APIRouter()

@router.get('/users/me')
def read_users_me(current_user=Depends(get_current_user)):
    # TODO: Implement logic to return current user info
    pass
