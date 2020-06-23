import pymongo
from datetime import datetime

def login_Screen():
    print("1.Login")
    print("2.Signup")

    menuSelect = input()
    if menuSelect == "1":
        login_user()
    if menuSelect == "2":
        signup_user()

def menu_Select():
    print("Please select operation to continue")
    print("1. Signup")
    print("2. Add book to database")
    print("3. Delete book from database")
    print("4. Search book in database")
    print("5. Borrow a book from library")
    print("6. Report borrowed books")
    print("7. Return a borrowed book")
    menuSelect = input()

    if menuSelect == "1":
        signup_user()
    if menuSelect == "2":
        add_book()
    if menuSelect == "3":
        delete_book()
    if menuSelect == "4":
        find_book("Sosyal Ağ Analizine Giriş","Yrd. Doç. Dr. Volkan Tunalı","","")
    if menuSelect == "5":
        borrow_book()
    if menuSelect == "6":
        borrow_report()
    if menuSelect == "7":
        return_book()
    elif int(menuSelect) > 7:
        print("Please select operation that exists !1-6!!!!! ")
        menuSelect = input()

def signup_user():
    print("Please enter your name")
    username = input()
    print("Please enter password")
    password = input()
    print("Please enter your email")
    email = input()
    print("Please enter your adress")
    adress = input()
    joined = datetime.now()

    user_dict = {
    "username"   : username, #String
    "password" : password, #String
    "email" : email, #String
    "adress" : adress, #String
    "joined" : joined #Datetime
    }

    x = myUsers.insert_one(user_dict)
    print("You have succesfully registered")
    print(x.inserted_id)

def borrow_report():
    cursor = myBorrows
    for document in cursor.find():
        print(document)

def borrow_book():
    print("Please enter your name")
    name = input()
    print("Please enter name of the book you want to borrow")
    borrowedbook = input()

    borrow_dict = {
    "name"   : name, #String
    "borrow-time" : datetime.now(), #Datetime
    "borrowed-book" : borrowedbook #String
    }

    x = myBorrows.insert_one(borrow_dict)
    print("You have succesfully borrowed a book")
    print("This is your borrow-id")
    print(x.inserted_id)

def return_book():
    print("Please enter your name")
    name = input()
    print("Please enter the name of the book you want to return")
    borrowedbook = input()

    borrow_dict = {
    "name" : name,
    "borrowed-book" : borrowedbook
    }

    myBorrows.delete_one(borrow_dict)
    print("You have succesfuly returned the book " + borrowedbook )

## CRUD OPERATIONS (1-ADD)
def add_book():
    print("If you dont know just skip that step !!!!!!")
    print("Please enter a book title")
    title = input()
    print("Please enter author name")
    author = input()
    print("Please enter editor name")
    editor = input()
    print("Please enter ISBN")
    ISBN = input()
    print("Please enter publish-year")
    publishyear = input()
    print("Please enter edition ")
    edition = input()
    print("Please enter publisher ")
    publisher = input()
    print("Please enter page count ")
    pagecount = input()
    print("Please enter language ")
    language = input()
    print("Please enter count ")
    count = input()

    book_dict = {
    "title"   : title, #String
    "authors" : author, #String
    "editors" : editor, #String
    "ISBN"    : ISBN, #String
    "publish-year" : publishyear, #Int32
    "edition" : edition, #String
    "publisher" : publisher, #String
    "page-count" : pagecount, #Int32
    "language" : language, #String
    "count"    : count #Int32
    }

    x = myBooks.insert_one(book_dict)
    print("You added book succesfuly")

## CRUD OPERATIONS (2-DELETE)
def delete_book():
    print("Please enter a book title")
    title = input()
    print("Please enter author name")
    author = input()
    print("Please enter ISBN")
    ISBN = input()

    book_search = {
    "title" : title
    }

    x = myBooks.delete_one(book_search)
    print("You have deleted the book with the name " + title + " written by " + author + "with the ISBN number: " + ISBN )

## CRUD OPERATIONS (3-READ)
def find_book(title, author, publishyear, edition):
    #print("Please select a data field to search for ...")
    #print("1. to search for title \n2. to search for author\n3. to search for editors\n4. to search for ISBN\n5. to search for publishyear\n6. to search for edition\n7. to search for publisher\n8. to search for pagecount\n9. to search for language\n10. to search for count")
    #datafield = input()
    book_search = {}
    if(title):
        book_search["title"] = title
    if(author):
        book_search["authors"] = author
    if(publishyear):
        book_search["publish-year"] = publishyear
    if(edition):
        book_search["edition"] = edition

    print(book_search)
    x = myBooks.find(book_search)
    print(x)

def search_book():
    print("Please select a data field to search for ...")
    print("1. to search for title \n2. to search for author\n3. to search for editors\n4. to search for ISBN\n5. to search for publishyear\n6. to search for edition\n7. to search for publisher\n8. to search for pagecount\n9. to search for language\n10. to search for count")
    datafield = input()
    print("Please enter a keyword or name for the search")
    forsearch = input()

    book_search = {
    datafield: forsearch
    }

    print(book_search)
    x = myBooks.find(book_search)


client = pymongo.MongoClient("mongodb+srv://ElektroJager:5651719s%%&@cluster0-yd4o5.gcp.mongodb.net/test?retryWrites=true&w=majority")
myDatabase = client["LibraryMS"]
myBooks = myDatabase["Books"]
myBorrows = myDatabase["Borrows"]
myUsers = myDatabase["Users"]

menu_Select()
