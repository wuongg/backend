from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import UserBase, UserCreate, UserRead, UserUpdate, PasswordReset, PasswordResetConfirm, UserLogin, Token
from app.deps import get_db
from app.models.user import User
from app.config.auth import create_access_token
from app.deps_auth import get_current_user
import bcrypt
import random
router = APIRouter(prefix="/users", tags=["users"])

@router.post('/', response_model=UserRead)
async def create_user(user_in: UserCreate, db: Session = Depends(get_db)):

    hashed_password = bcrypt.hashpw(user_in.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    if db.query(User).filter(User.email == user_in.email).first():
        raise HTTPException(status_code=400, detail="Email already registered")

    user = User(
        email=user_in.email, 
        last_name=user_in.last_name, 
        first_name=user_in.first_name, 
        phone=user_in.phone, 
        date_of_birth=user_in.date_of_birth, 
        gender=user_in.gender, 
        role=user_in.role, 
        hashed_password=hashed_password)
    try:    
        db.add(user)
        db.commit()
        db.refresh(user)
        return user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e))

@router.post('/login', response_model=Token)
async def login(user_in: UserLogin, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.email == user_in.email).first()

    if not user:
        raise HTTPException(status_code=400, detail="Invalid email or password")

    if not bcrypt.checkpw(user_in.password.encode('utf-8'), user.hashed_password):
        raise HTTPException(status_code=400, detail="Invalid email or password")
    
    access_token = create_access_token(user.model_dump())

    return Token(access_token=access_token, token_type="Bearer")

@router.get('/{user_id}', response_model=UserRead)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    return user

@router.get('/me', response_model=UserRead)
async def read_me(current_user: User = Depends(get_current_user)):
    return current_user