from fastapi import APIRouter, HTTPException, status

from src.models.request import auth as requestModels
from src.models.response import auth as responseModels
from src.database.schemas.user import User
from src.utils.auth import pwd_context, verify_password, get_password_hash
from src.database.crud import users as crud

authRouter = APIRouter()

@authRouter.post("/signup")
async def signup(user: requestModels.SignupUser):
    """ create new user return access and refresh token
    """
    if user.password != user.confirmPassword:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Passwords don't match")

    # hash password
    hashed_password = get_password_hash(user.password)
    
    # save user
    new_user = crud.create_user(User, user, hashed_password)
    print(new_user)
    

    # generate and return tokens
    pass

@authRouter.post("/token")
async def token(user: requestModels.LoginUser):
    """ authenticate user and return access and refresh token
    """
    # search for user
    # validate password
    # generate and return tokens

@authRouter.post("/refreshToken", response_model= responseModels.Tokens)
async def refresh_token():
    """ try refreshing access token if refresh token still valid
    """
    # validate refresh token
    # if valid, return new set of tokens
    # if not, return unauthorized
