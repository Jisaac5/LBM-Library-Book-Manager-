import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Frames.viewBooks import *
from Frames.BorrowReturn import *

def viewDelete(Frame9,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5,Frame6,Frame1,Frame8,Frame10):

    def libFetch(searchKeyword):
        # Fetch data from db
        dbconn = sqlite3.connect("Library.db")
        dbcursor = dbconn.cursor()

        if searchKeyword == '':
            dbcursor.execute("SELECT rowid, * FROM books")
            LibItems = dbcursor.fetchall()
        else:
            dbcursor.execute("""SELECT rowid, * FROM books WHERE (
                name LIKE '%{}%' OR
                author LIKE '%{}%' OR
                date LIKE '%{}%' OR
                genre1 LIKE '%{}%' OR
                genre2 LIKE '%{}%' OR
                genre3 LIKE '%{}%'
                )""".format(searchKeyword, searchKeyword, searchKeyword, searchKeyword, searchKeyword, searchKeyword))
            LibItems = dbcursor.fetchall()

        dbconn.commit()
        dbconn.close()

        return LibItems

    def libInject(LibItems):
        # Insert into treeview
        for item in libTree.get_children():
            libTree.delete(item)
        for item in LibItems:
            genres = item[4] + ', ' + item[5] + ', ' + item[6]
            libTree.insert(parent='', index='end', iid=item[0] - 1, text="",
                        values=(item[0], item[1], item[2], item[3], genres))


        searchBar.delete(0, "end")

    def OnDoubleClick(event):
        item = str(libTree.selection())
        transitionString = item.replace('(\'', " ")
        removeSpace = transitionString.replace('\',)', ' ')
        myString = removeSpace.strip()
        rowID = (int(myString) + 1)

        suggAction(rowID)

    def suggAction(rowID):
        dbconn = sqlite3.connect("Library.db")
        dbcursor = dbconn.cursor()

        dbcursor.execute("SELECT rowid, * FROM books WHERE rowid ='{}'".format(rowID))

        dbconn.commit()

        suggBook = dbcursor.fetchone()

        choice = messagebox.askyesno(title='Delete Book',
                                     message=('Would you like to delete ' + suggBook[
                                         1] + ' from the Library?'))

        if choice == True:
            dbcursor.execute("DELETE FROM books WHERE rowid = '{}'".format(rowID))
            dbconn.commit()
            libInject(libFetch(searchBar.get()))

        dbconn.close()

        viewBooks(Frame6,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame8)
        borrowReturn(Frame10,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1)

    Canvas1 = Canvas(Frame9, width=1100, height=650)
    Canvas1.create_image(0, 0, image=img, anchor="nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    # Treeview frame
    tree_frame = Frame(Frame9)
    tree_frame.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.75)

    style = ttk.Style()
    style.configure("Treeview",
                    background="#d8b785",
                    foreground="black",
                    rowheight=30,
                    font=("Arial Black", 10),
                    fieldground="d8b785"
                    )
    # Initialize treeview
    libTree = ttk.Treeview(tree_frame)
    # Place
    libTree.place(relx=0, rely=0, relwidth=1, relheight=1)

    # Treeview scrollbar
    tree_scroll = Scrollbar(tree_frame, orient='vertical', command=libTree.yview)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_Scrollx = Scrollbar(tree_frame, orient='horizontal', command=libTree.xview)
    tree_Scrollx.pack(side=BOTTOM, fill=X)

    libTree.configure(xscrollcommand=tree_Scrollx.set)
    libTree.configure(yscrollcommand=tree_scroll.set)

    # Define columns
    libTree['columns'] = ("ID", "Title", "Author", "Published", "Genres")

    # Format columns
    libTree.column("#0", width=0, stretch=NO)
    libTree.column("ID", anchor=W, width=30, minwidth=20, stretch=NO)
    libTree.column("Title", anchor=W, width=600, minwidth=20)
    libTree.column("Author", anchor=W, width=220, minwidth=20)
    libTree.column("Published", anchor=W, width=120, minwidth=20, stretch=NO)
    libTree.column("Genres", anchor=W, width=450, minwidth=20)

    # Create headings
    libTree.heading("#0", text="", anchor=W)
    libTree.heading("ID", text="ID", anchor=W)
    libTree.heading("Title", text="Title", anchor=W)
    libTree.heading("Author", text="Author", anchor=W)
    libTree.heading("Published", text="Published", anchor=W)
    libTree.heading("Genres", text="Genres", anchor=W)

    # Search bar
    searchBar = Entry(Frame9, bg="#d8b785", bd=2, font=('Constantia',12))
    searchBar.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.05)

    # Search Button
    searchBtn = Button(Frame9, text="Search", bg='#d8b785', fg='#3D2B1F', font=("Cooper Black", 10),
                       command=lambda: libInject(libFetch(searchBar.get())))
    searchBtn.place(relx=0.45, rely=0.1, relwidth=0.1)

    libTree.bind("<Double-1>", OnDoubleClick)
    # Prevent resizing of columns
    libTree.bind('<Motion>', 'break')

    libInject(libFetch(''))

    btn1 = Button(Frame9, text="Back", bg='#d8b785', fg='#3D2B1F', font=("Cooper Black", 12),
                  command=lambda: showFrame(Frame5))
    btn1.place(relx=0.01, rely=0.05, relwidth=0.15, relheight=0.06)