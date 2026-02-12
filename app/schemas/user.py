"""
SCHEMA USER (Pydantic)
----------------------

File này để bạn thực hành:
- Tạo các schema để validate dữ liệu vào/ra cho User.

Gợi ý các schema thường gặp:
- UserBase: chứa các field chung (email, is_active, ...)
- UserCreate: dùng cho đăng ký (thêm password)
- UserRead / UserOut: dữ liệu trả về cho client (không có password)
"""

from pydantic import BaseModel, EmailStr, Field, field_validator
from datetime import date, datetime


class UserBase(BaseModel):
    """TODO: thêm các field chung cho User (ví dụ: email)."""

    # ví dụ:
    # email: EmailStr
    email: EmailStr = Field(..., description="Email of the user")
    last_name: str = Field(..., description="Last name of the user")
    first_name: str= Field(..., description="First name of the user")
    phone: str = Field(...,regex=r"^0[0-9]{9}$",description="Phone of the user")
    date_of_birth: date = Field(None, description="Date of birth of the user")
    gender: str = Field(...,regex=r"^male|female|other$",description="Gender of the user")
    role:str = Field(...,regex=r"^admin|user$",description="Role of the user")

    

class UserCreate(UserBase):
    """TODO: thêm password để dùng khi đăng ký."""

    # ví dụ:
    # password: str
    password: str = Field(...,min_length=8,description="Password of the user")
    re_password: str = Field(...,min_length=8,description="Re-password of the user")

    @field_validator("re_password")
    def check_password(cls, v, info):
        password = info.data.get("password")
        if password is not None and v != password:
            raise ValueError("Password and re-password do not match")
        return v

class UserRead(UserBase):
    """TODO: schema trả về cho client (không có password)."""

    # ví dụ:
    # id: int
    # is_active: bool
    id:int = Field(...,description="ID of the user")
    is_active:bool = Field(...,description="Is active of the user")
    created_at:datetime = Field(...,description="Created at of the user")
    updated_at:datetime = Field(...,description="Updated at of the user")

class UserInDB(UserBase):
    hashed_password:str = Field(...,description="Hashed password of the user")

class PasswordReset(BaseModel):
    email:EmailStr = Field(...,description="Email of the user")

class PasswordResetConfirm(BaseModel):
    email:EmailStr = Field(...,description="Email of the user")
    code:str = Field(...,description="Code of the user")
    new_password:str = Field(...,min_length=8,description="New password of the user")
    re_new_password:str = Field(...,min_length=8,description="Re-new password of the user")
    @field_validator("re_new_password")
    def check_password(cls, v, info):
        new_password = info.data.get("new_password")
        if new_password is not None and v != new_password:
            raise ValueError("New password and re-new password do not match")
        return v

class UserLogin(BaseModel):
    email:EmailStr = Field(...,description="Email of the user")
    password:str = Field(...,min_length=8,description="Password of the user")

class Token(BaseModel):
    access_token:str = Field(...,description="Access token of the user")
    token_type:str = Field(...,description="Token type of the user")