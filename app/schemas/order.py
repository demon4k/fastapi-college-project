from pydantic import BaseModel


class OrderCreate(BaseModel):
    total_price: float
    user_id: int


class OrderResponse(BaseModel):
    id: int
    total_price: float
    user_id: int

    class Config:
        from_attributes = True