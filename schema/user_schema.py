from lib2to3.pgen2.token import OP
from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    id: Optional[str]
    name: str
    username: str
    user_pwd: str


class DataUser(BaseModel):
    username: str
    user_pwd: str