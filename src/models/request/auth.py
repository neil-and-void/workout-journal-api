from pydantic import BaseModel
from pydantic.networks import EmailStr

class SignupUser(BaseModel):
    email: EmailStr
    password: str
    confirmPassword: str
    name: str

class LoginUser(BaseModel):
    email: EmailStr
    password: str
