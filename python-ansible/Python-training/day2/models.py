from sqlalchemy import Column, String
from database import Base

class Userapp(Base):
    __tablename__ = 'USERAPP'

    username = Column(String, primary_key = True)
    email = Column(String)
    city = Column(String)