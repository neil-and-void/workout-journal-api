from fastapi import Header

def verifyRefreshToken(x_token: str = Header(...)):
    pass
