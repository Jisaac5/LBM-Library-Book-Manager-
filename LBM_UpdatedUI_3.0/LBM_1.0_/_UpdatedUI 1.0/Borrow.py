import sqlite3

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

def switchStatus():

    dbcursor.execute("SELECT status FROM books WHERE rowid = {}" .format(switchChoice))
    
    switch = dbcursor.fetchone()

    if switch == ('available',):
        dbcursor.execute("UPDATE books SET status = 'borrowed' WHERE rowid = {}".format(switchChoice))
        print('IT IS AVAILABLE')
    elif switch == ('borrowed',):
        dbcursor.execute("UPDATE books SET status = 'available' WHERE rowid = {}".format(switchChoice))
        print('IT IS BORROWED')
    else:
        print('Something Went Wrong')


    dbconn.commit()
    dbconn.close()

view()
switchChoice = input('ENTER ROW ID: ')
print(switchChoice)
switchStatus()
input()
