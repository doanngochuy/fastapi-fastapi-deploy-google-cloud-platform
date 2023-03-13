from typing import Optional
from pydantic import BaseModel


class JobBase(BaseModel):
    key_word: str
    image: str
    total: int
    count: int
    url: str
    time: int


class JobCreate(JobBase):
    key_page: str
    value_page: str
    pass


class JobItemResponse(JobBase):
    id: int

    # users = relationship("User")
    class Config:
        orm_mode = True


class JobStart(JobBase):
    id: int
    user_id: int
    current_id: int
