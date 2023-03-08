from typing import List

from pydantic import BaseModel


class UserCreateInput(BaseModel):
    name: str


class StandardOutput(BaseModel):
    message: str


class ErrorOutPut(StandardOutput):
    detail: str


class UserFavoriteAddInput(BaseModel):
    user_id: int
    symbol: str


class Favorite(BaseModel):
    id: int
    symbol: str
    user_id: int

    class Config:
        orm_mode = True


class UserListoutput(BaseModel):
    id: int
    name: str
    favorites: List[Favorite]

    class Config:
        orm_mode = True


class DaySumaryOutput(BaseModel):
    highest: float
    lowest: float
    symbol: str
