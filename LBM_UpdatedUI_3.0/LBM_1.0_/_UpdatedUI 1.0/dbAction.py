import sqlite3
import os


class Book:
    name = ""
    author = ""
    date = ""
    genre1 = ""
    genre2 = ""
    genre3 = ""
    status = ""
    synopsis = ""

dbconn=sqlite3.connect('Library.db')

dbcursor=dbconn.cursor()

BookInfo=Book()

class BookComm:
    #Create table in database
    def createtable():
        dbcursor.execute("""CREATE TABLE books
        (
            name text,
            author text,
            date text,
            genre1 text,
            genre2 text,
            genre3 text,
            status text,
            synopsis text
        )""")
        dbconn.commit()
        dbconn.close

    #Insert book into database
    def insertbookinfo():
        dbcursor.execute("INSERT INTO books VALUES (?,?,?,?,?,?,?,?)", (BookInfo.name, BookInfo.author, BookInfo.date, BookInfo.genre1, BookInfo.genre2, BookInfo.genre3, BookInfo.status, BookInfo.synopsis))
        dbconn.commit()
        dbconn.close

    #Show all library contents
    def view():
        dbcursor.execute("SELECT rowid, * FROM books")
        
        items = dbcursor.fetchall()

        for item in items:
            print('STATUS:' + str(item[7]))
            print('Book ' + str(item[0]))
            print('Book Name: ' + str(item[1]))
            print('Book Author: ' + item[2])
            print('Book Date Published: ' + str(item[3]))
            print('Book Genres: ' + item[4] + ', ' + item[5] + ', ' + item[6])
            print('SYNOPSIS:')
            print(item[8] + '\n\n')


        dbconn.commit()
        dbconn.close

    #Search for a book
    def viewSpecific(filter, keyword):
        dbcursor.execute("SELECT rowid, * FROM books WHERE filter LIKE %keyword OR keyword%")
        
        items = dbcursor.fetchall()

        # for item

    #Delete all content from "books" table
    def deleteall():
        dbcursor.execute("DELETE FROM books")
        dbconn.commit()
        dbconn.close

    #Delete specific book
    def delete(number):
        dbconn=sqlite3.connect('Library.db')
        dbcursor=dbconn.cursor()

        dbcursor.execute("DELETE FROM books WHERE rowid ={}" .format(number))
        dbconn.commit()
        dbconn.close()

    def gatherInfo():
        BookInfo.name = input('Book Name: ')
        BookInfo.author = input('Book Author: ')
        BookInfo.date = input('Book Date: ')
        BookInfo.genre1 = input('Book Genre1: ')
        BookInfo.genre2 = input('Book Genre2: ')
        BookInfo.genre3 = input('Book Genre3: ')
        BookInfo.synopsis = input('Book Synopsis: ')
        BookInfo.status = input('Book Status: ')

    def inputInfo():
        BookComm.gatherInfo()
        BookComm.insertbookinfo()

    def loopGather():
        loop = 1
        while loop == 1:
            BookComm.inputInfo()
            print("successfully added into library")
            choice = input('Add another book?(y/n)')
            if choice == 'y':
                os.system('CLS')
            else:
                break    

    def update():
        dbcursor.execute("""UPDATE books SET rowid = 28  
                            WHERE rowid = 29
        """)

        dbconn.commit()
        dbconn.close()

class SuggComm:
    class Suggest:
        name = ""
        book = ""
        author = ""

    suggestion = Suggest()

    def createtable():
        dbcursor.execute("""CREATE TABLE suggestions
        (
            book text,
            name text,
            author text
        )""")
        dbconn.commit()
        dbconn.close

    def gatherInfo():
        SuggComm.suggestion.name = input('Enter your name: ')
        SuggComm.suggestion.book = input('What book would you like to suggest to our library? : ')
        SuggComm.suggestion.author = input('Who is the author? : ')


    def insertsuggestioninfo():
        dbcursor.execute("INSERT INTO suggestions VALUES (?,?,?)",(SuggComm.suggestion.book, SuggComm.suggestion.name, SuggComm.suggestion.author))
        dbconn.commit()
        dbconn.close

    def delete(number):
        dbconn=sqlite3.connect('Library.db')

        dbcursor=dbconn.cursor()

        dbcursor.execute("DELETE FROM suggestions WHERE rowid ={}" .format(number))
        dbconn.commit()
        dbconn.close()


    def inputInfo():
        SuggComm.gatherInfo()
        SuggComm.insertsuggestioninfo()

    def view():
        dbcursor.execute("SELECT rowid, * FROM suggestions")
        print(dbcursor.fetchall())

    def loopInput():
        loop = 1
        while loop == 1:
            SuggComm.inputInfo()
            choice = input('Would you like to add another suggestion? (y/n): ')
            if choice != 'y':
                break

BookComm.update()
input()