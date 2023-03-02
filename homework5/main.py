from enum import Enum
from http.client import FOUND
from fastapi import FastAPI,Depends,Query
from requests import Session
from sqlalchemy import false, null
from database import engine, SessionLocal
import uvicorn
import nest_asyncio
import crud
import models

#initailize FastApi instance
app = FastAPI()

#create the database tables on app startup or reload
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#get show all
@app.get("/Books")
def list_book(db:Session = Depends(get_db)):
    book_list = crud.list_Bookstore(db=db)
    return book_list

#get show by Name
@app.get("/Books/Name/{Name}") #id is a path parameter
def get_book(Book_title:str, db:Session = Depends(get_db)):
    book = crud.get_Bookstorebyname(db, Book_title=Book_title)
    print(book)
    return book

#get show by id
@app.get("/Books/{id}") #id is a path parameter
def get_book(id:int, db:Session = Depends(get_db)):
    book = crud.get_Bookstorebyid(db, id)
    return book

#insert book
@app.post("/Books/{id}")
def create_book(Book_ISBN:int ,Book_title:str, Author:str, Price:int, Qty:int, db:Session = Depends(get_db)):
    book = crud.create_Bookstore(db=db, Book_ISBN=Book_ISBN, Book_title=Book_title, Author=Author, Price=Price, Qty=Qty)
##return object created
    if book:
        return {"book": book}
    else:
        return {"error": f"book with Book_ISBN {Book_ISBN} does not exist"}

#update book 
@app.put("/Books/{id}") #id is a path parameter
def update_book(id:int, Book_ISBN:int ,Book_title:str, Author:str, Price:int, Qty:int, db:Session = Depends(get_db)):
    #get book object from database
    book = crud.get_Bookstorebyid(db, id)
    #check if book object exists
    if book:
        updated_book = crud.update_Bookstore(db, id, Book_ISBN=Book_ISBN, Book_title=Book_title, Author=Author, Price=Price, Qty=Qty)
        return updated_book
    else:
        return {"error": f"book with id {id} does not exist"}

#delete by id
@app.delete("/Books/{id}") #id is a path parameter
def delete_book(id:int, db:Session = Depends(get_db)):
    #get book object from database
    db_book = crud.get_Bookstorebyid(db, id)
    #check if book object exists
    if db_book:
        return crud.delete_Bookstore(db, id)
    else:
        return {"error": f"book with id {id} does not exist"}


    
@app.get("/Books/Price/{prince}")
def get_price(prince:int,option_price:str = Query("MORE", enum=["MORE", "LESS", "EQUAL"]) ,db:Session = Depends(get_db)):
    db_book = crud.get_price(db, prince, option_price)
    print(db_book)
    if db_book == false:
        return {"error": f"No book Price {prince} is {option_price} "}
    
    elif db_book:
        return db_book
    else:
        return {"error": f"No book Price {prince} is {option_price} "}
nest_asyncio.apply()
uvicorn.run(app, port=8080)




