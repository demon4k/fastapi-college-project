from pydantic import BaseModel


class ProfileCreate(BaseModel):
    bio: str
    phone: str
    user_id: int


class ProfileResponse(BaseModel):
    id: int
    bio: str
    phone: str
    user_id: int

    class Config:
        from_attributes = True