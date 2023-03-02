import sqlite3
from sqlalchemy import false, null
from sqlalchemy.orm import Session
from models import Bookstore


def create_Bookstore(db:Session, Book_ISBN, Book_title, Author, Price, Qty):
    """
    function to create a book model object
    """
      # create book. instance 
    new_book = Bookstore(Book_ISBN=Book_ISBN, Book_title=Book_title, Author=Author, Price=Price, Qty=Qty)
        #place object in the database session
    db.add(new_book)
        #commit your instance to the database
    db.commit()
        #reefresh the attributes of the given instance
    db.refresh(new_book)
    return new_book

#get book by id
def get_Bookstorebyid(db:Session, Book_id:int):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_book = db.query(Bookstore).filter(Bookstore.Book_id==Book_id).first()
    return db_book

#get book by name
def get_Bookstorebyname(db:Session, Book_title:str):
    """
    get the first record with a given id, if no such record exists, will return null
    """
    db_book = db.query(Bookstore).filter(Bookstore.Book_title==Book_title).first()
    return db_book

def list_Bookstore(db:Session):
    """
    Return a list of all existing Friend records
    """
    all_book = db.query(Bookstore).all()
    return all_book


def update_Bookstore(db:Session, Book_id:int,Book_ISBN: int, Book_title: str, Author: str, Price:int, Qty:int):
    """
    Update a bookstore object's attributes
    """
    db_book = get_Bookstorebyid(db=db, Book_id=Book_id)
    db_book.Book_ISBN = Book_ISBN
    db_book.Book_title = Book_title
    db_book.Author = Author
    db_book.Price = Price
    db_book.Qty = Qty

    db.commit()
    db.refresh(db_book) #refresh the attribute of the given instance
    return db_book

def delete_Bookstore(db:Session, Book_id:int):
    """
    Delete a Bookstore object
    """
    db_book = get_Bookstorebyid(db=db, Book_id=Book_id)
    db.delete(db_book)
    db.commit() #save changes to db


def get_price(db:Session, prince:int, option_price:str):
    print(option_price)
    
    if option_price == " ":
        db_book = db.query(Bookstore,Bookstore.Price).all()

    elif option_price == "MORE":
        db_book = db.query(Bookstore,Bookstore.Price).filter(Bookstore.Price > prince).all()

    elif option_price == "LESS":
        db_book = db.query(Bookstore,Bookstore.Price).filter(Bookstore.Price < prince).all()
        
    elif option_price == "EQUAL":
        db_book = db.query(Bookstore,Bookstore.Price).filter(Bookstore.Price == prince).all()

    else:
        return false
    
    return db_book