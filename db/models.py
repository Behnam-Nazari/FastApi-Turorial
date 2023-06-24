
from sqlalchemy import Column, Integer, String
from db.database import Base


class DbUSer(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100))
    email = Column(String)
    password = Column(String)
