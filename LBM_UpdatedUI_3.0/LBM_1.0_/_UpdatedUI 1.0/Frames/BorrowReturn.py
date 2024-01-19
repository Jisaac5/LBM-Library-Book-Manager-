import sqlite3
from Frames.BookInfo import *
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def borrowReturn(Frame10,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1):

    def OnDoubleClick(event):
        item = str(libTree.selection())
        transitionString = item.replace('(\''," ")
        removeSpace = transitionString.replace('\',)',' ')
        myString = removeSpace.strip()
        rowID = (int(myString)+1)
        
        mainAction(rowID)

    def mainAction(rowID):
        dbconn = sqlite3.connect("Library.db")
        dbcursor = dbconn.cursor()

        dbcursor.execute("SELECT rowid, * FROM books WHERE rowid = {}" .format(rowID))

        dbconn.commit()
        
        bookList = dbcursor.fetchone()
        bookChoice = bookList[7]
        bookName = bookList[1]

        if bookChoice == 'available':
           messageInput = messagebox.askyesno(title='Borrow Book',
                            message= ('Would you like to borrow ' + str(bookName.strip()) + '?'))
        elif bookChoice == 'borrowed':
           messageInput = messagebox.askyesno(title='Return Book',
                            message= ('Would you like to return ' + str(bookName.strip()) + ' to the Library?'))
        else:
            print("CANNOT READ?A????A???")

        if messageInput == True and bookChoice == 'available':
            dbcursor.execute("UPDATE books SET status = 'borrowed' WHERE rowid = {}".format(rowID))
        if messageInput == True and bookChoice == 'borrowed':
            dbcursor.execute("UPDATE books SET status = 'available' WHERE rowid = {}".format(rowID))

        dbconn.commit()

        libInject(libFetch(searchBar.get()))

        
            
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
                status LIKE '%{}%'
                )""".format(searchKeyword, searchKeyword, searchKeyword))
            LibItems = dbcursor.fetchall()

        dbconn.commit()
        dbconn.close()
        
        return LibItems

    def libInject(LibItems):
        for item in libTree.get_children():
            libTree.delete(item)
        # Insert into treeview
        for item in LibItems:
            libTree.insert(parent='', index='end', iid=item[0] - 1, text="",
                        values=(item[0], item[1], item[7]))

        libTree.bind("<Double-1>", OnDoubleClick)
    
    
    Canvas1 = Canvas(Frame10,width=1100,height=650)

    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    #Treeview frame
    tree_frame = Frame(Frame10)
    tree_frame.place(relx=0.05,rely=0.15, relwidth=0.9, relheight=0.75)


    style = ttk.Style()
    style.configure("Treeview",
                    background = "#d8b785",
                    foreground = "black",
                    rowheight  = 30,
                    font =("Arial Black",10),
                    fieldground = "d8b785"

                    )
    #Initialize treeview
    libTree = ttk.Treeview(tree_frame)


    #Place
    libTree.place(relx=0,rely=0, relwidth=1, relheight=1)

    #Treeview scrollbar
    tree_scroll = Scrollbar(tree_frame, orient='vertical', command=libTree.yview)
    tree_scroll.pack(side=RIGHT, fill=Y)

    libTree.configure(yscrollcommand=tree_scroll.set)

    #Define columns
    libTree['columns'] = ("ID", "Title", "Status")

    #Format columns
    libTree.column("#0", width=0, stretch=NO)
    libTree.column("ID", anchor=W, width=30, minwidth=20, stretch=NO)
    libTree.column("Title", anchor=W, width=600, minwidth=20)
    libTree.column("Status", anchor=W, width=220, minwidth=20)

    #Create headings
    libTree.heading("#0", text="", anchor=W)
    libTree.heading("ID", text="ID", anchor=W)
    libTree.heading("Title", text="Title", anchor=W)
    libTree.heading("Status", text="Status", anchor=W)


    libTree.bind('<Motion>', 'break')
    libTree.bind("<Double-1>", OnDoubleClick)


    
    #Search bar
    searchBar = Entry(Frame10, bg="#d8b785", bd=2, font=('Constantia',12))
    searchBar.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.05)

    #Search Button
    searchBtn = Button(Frame10, text="Search", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",10), command=lambda:libInject(libFetch(searchBar.get())))
    searchBtn.place(relx=0.45, rely=0.1, relwidth=0.1)

    libInject(libFetch(''))

    btn1 = Button(Frame10, text="Back", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",12),command=lambda:showFrame(Frame1))
    btn1.place(relx=0.01, rely=0.05, relwidth=0.15, relheight=0.06)