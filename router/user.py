from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm.session import Session
from db import db_user

from schemas import UserBase

router = APIRouter(
    prefix="/user",
    tags=['user']
)


#Create
@router.post('/')
def create_user(request:UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


#Read


#Update


#Delete