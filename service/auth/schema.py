from typing import Optional

from pydantic import BaseModel


class RegisterReq(BaseModel):
    username: str
    password: str
    full_name: str

    def validate(self):
        if not self.username or not self.password or not self.full_name:
            raise ValueError("username, password, and full_name are required fields")

class Token(BaseModel):
    access_token: str
    token_type: str
    username: str
    role: str


class AuthRes(BaseModel):
    message: str
    user: Optional[dict] = None
