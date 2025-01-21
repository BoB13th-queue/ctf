from pydantic import BaseModel


class User(BaseModel):
    username: str
    full_name: str
    role: str

class UserRes(User):
    id: int


class UserList(BaseModel):
    cnt: int
    page: int
    limit: int
    users: list[UserRes]