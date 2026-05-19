from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True)
    age: Mapped[int]
    hashed_password: Mapped[str] = mapped_column(String(255), default="")

    profile = relationship("Profile", back_populates="user", uselist=False)
    orders = relationship("Order", back_populates="user")