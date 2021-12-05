from fastapi import APIRouter

authRouter = APIRouter()

@authRouter.post("/auth/signup")
async def signup():
    """ create new user return access and refresh token
    """
    pass

@authRouter.post("/auth/token")
async def token():
    """ authenticate user and return access and refresh token
    """
    pass

@authRouter.post("/auth/refreshToken")
async def refresh_token():
    """ try refreshing access token if refresh token still valid
    """
    pass