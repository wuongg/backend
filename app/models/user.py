"""
MODEL USER (ORM)
----------------

File này để bạn thực hành:
- Định nghĩa model User với ORM (ví dụ: SQLAlchemy)
- Mapping với bảng trong database (users)
"""

# TODO:
# - Cài SQLAlchemy (nếu chưa): pip install sqlalchemy
# - Tạo Base trong `app/db/__init__.py` hoặc file riêng (ví dụ: base.py)
# - Import Base vào đây và tạo class User(Base)

# Ví dụ khung (bạn tự hoàn thiện):
#
# from sqlalchemy import Column, Integer, String
# from app.db import Base  # TODO: tạo Base trước
#
# class User(Base):
#     __tablename__ = "users"
#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True, nullable=False)
#     hashed_password = Column(String, nullable=False)
#     is_active = Column(Boolean, default=True)
#
from sqlalchemy import Column, Integer, String, Boolean, Date, Enum, DateTime
from datetime import datetime, date
from app.db import Base
class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True,index=True)

    email = Column(String, unique=True, index=True, nullable=False)
    last_name = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    date_of_birth = Column(Date, nullable=False)
    gender = Column(
        Enum("male", "female", "other", name="gender_enum"), 
        nullable=False)
    role = Column(
        Enum("admin", "user", name="role_enum"), 
        nullable=False)

    hashed_password = Column(String, nullable=False)

    is_active = Column(Boolean, default=True, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(
        DateTime, 
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        nullable=False)



