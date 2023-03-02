from sqlalchemy import Column, Integer, String
from database import Base

# model/table
class Bookstore(Base):
    __tablename__ = "bookstore"

    # fields 
    Book_id  = Column(Integer,primary_key=True, index=True, autoincrement=True)
    Book_ISBN  = Column(Integer, unique=True, index=True)
    Book_title = Column(String)
    Author = Column(String)
    Price  = Column(Integer)
    Qty  = Column(Integer)