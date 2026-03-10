from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String


class Base(DeclarativeBase):
    """Базовый класс для всех моделей."""
    pass


class Account(Base):
    __tablename__ = "accounts"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    owner_id: Mapped[str] = mapped_column(String(36), nullable=False, index=True)
    currency: Mapped[str] = mapped_column(default=0)
    version: Mapped[int] = mapped_column(default=0, nullable=False)
