import sqlite3 as sql
db = None
cursor = None

def initDB(filename = None):
    global db, cursor
    if not filename:
        filename = 'my.db'
    try:
        db = sql.connect(filename)
        cursor = db.cursor()
    except:
        print("Error connecting to", filename)
        cursor = None
        raise

def closeDB():
    print("Close Lab")
    cursor.close()
    db.commit()
    db.close()

def getAuthorID(authorName=None):
    if not authorName :
        query = "select ID from author"
        cursor.execute(query)
    else :
        query = "select ID from author where name like ?"
        cursor.execute(query,(authorName,))
    return cursor.fetchall()

def getAuthorIDBook(bookName=None):
    if not bookName :
        query = "select ID from book"
        cursor.execute(query)
    else :
        query = "select Title from book where title like ?"
        cursor.execute(query,(bookName,))
    return cursor.fetchall()


if __name__ == "__main__" :
    initDB()
    print(getAuthorIDBook("Emma"))
    closeDB()