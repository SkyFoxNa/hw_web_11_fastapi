from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, Date
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Contact(Base):
    __tablename__ = 'contacts'

    id: Mapped[int] = mapped_column(primary_key = True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False, index = True)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False,  index = True)
    email: Mapped[str] = mapped_column(String(100), nullable=False, index = True)
    phone_number: Mapped[str] = mapped_column(String(20), index = True)
    birthday: Mapped[Date] = mapped_column(Date, nullable=False)
    address: Mapped[str] = mapped_column(String(250))
    notes: Mapped[str] = mapped_column(String(250))
    interests: Mapped[str] = mapped_column(String(250))
    is_active: Mapped[bool] = mapped_column(default=False)
