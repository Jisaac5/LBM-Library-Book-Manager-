import sqlite3
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def viewSuggestions(Frame7,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5):

    def libFetch(searchKeyword):
        # Fetch data from db
        dbconn = sqlite3.connect("Library.db")
        dbcursor = dbconn.cursor()

        if searchKeyword == '':
            dbcursor.execute("SELECT rowid, * FROM suggestions")
            LibItems = dbcursor.fetchall()
        else:
            dbcursor.execute("""SELECT rowid, * FROM suggestions WHERE (
                name LIKE '%{}%' OR
                author LIKE '%{}%' OR
                book LIKE '%{}%'
                )""".format(searchKeyword, searchKeyword, searchKeyword))
            
            LibItems = dbcursor.fetchall()

        dbconn.commit()
        dbconn.close()

        return LibItems


    def libInject(LibItems):
        # Insert into treeview
        for item in libTree.get_children():
            libTree.delete(item)
        for item in LibItems:
            libTree.insert(parent='', index='end', iid=item[0] - 1, text="",
                        values=(item[0], item[1], item[3], item[2]))
        
        searchBar.delete(0, "end")

    def OnDoubleClick(event):
        item = str(libTree.selection())
        transitionString = item.replace('(\''," ")
        removeSpace = transitionString.replace('\',)',' ')
        myString = removeSpace.strip()
        rowID = (int(myString)+1)
        
        suggAction(rowID)

    def suggAction(rowID):
        dbconn = sqlite3.connect("Library.db")
        dbcursor = dbconn.cursor()

        dbcursor.execute("SELECT rowid, * FROM suggestions WHERE rowid ='{}'".format(rowID))

        dbconn.commit()
        
        suggBook = dbcursor.fetchone()

        choice = messagebox.askyesno(title='Delete Suggestion',
                            message= ('Would you like to delete ' + suggBook[1] + ' from the suggestions list?'))

        if choice == True:
            dbcursor.execute("DELETE FROM suggestions WHERE rowid = '{}'".format(rowID))
            dbconn.commit()
            libInject(libFetch(''))


        dbconn.close()



    Canvas1 = Canvas(Frame7,width=1100,height=650)
    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    #Treeview frame
    tree_frame = Frame(Frame7)
    tree_frame.place(relx=0.05,rely=0.15, relwidth=0.9, relheight=0.75)
    
    #Initialize treeview    
    libTree = ttk.Treeview(tree_frame)
    #Place
    libTree.place(relx=0,rely=0, relwidth=1, relheight=1)

    #Treeview scrollbar
    tree_scroll = Scrollbar(tree_frame, orient='vertical', command=libTree.yview)
    tree_scroll.pack(side=RIGHT, fill=Y)

    libTree.configure(yscrollcommand=tree_scroll.set)

    # Define columns
    libTree['columns'] = ("ID", "Book", "Author", "Suggestor")

    # Format columns
    libTree.column("#0", width=0, stretch=NO)
    libTree.column("ID", anchor=W, width=20, minwidth=20, stretch=NO)
    libTree.column("Book", anchor=W, width=300, minwidth=150, stretch=NO)
    libTree.column("Author", anchor=W, width=280, minwidth=150, stretch=NO)
    libTree.column("Suggestor", anchor=W, width=320, minwidth=150, stretch=NO)

    # Create headings
    libTree.heading("#0", text="", anchor=W)
    libTree.heading("ID", text="ID", anchor=W)
    libTree.heading("Book", text="Title", anchor=W)
    libTree.heading("Author", text="Author", anchor=W)
    libTree.heading("Suggestor", text="Suggestor", anchor=W)




    
    #Search bar
    searchBar = Entry(Frame7, bg="#d8b785", bd=2, font=('Constantia',12))
    searchBar.place(relx=0.25, rely=0.04, relwidth=0.5, relheight=0.05)


    #Search Button
    searchBtn = Button(Frame7, text="Search", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",10), command=lambda:libInject(libFetch(searchBar.get())))
    searchBtn.place(relx=0.45, rely=0.1, relwidth=0.1)

    libTree.bind("<Double-1>", OnDoubleClick)
    #Prevent resizing of columns
    libTree.bind('<Motion>', 'break')        

    libInject(libFetch(''))

    btn1 = Button(Frame7, text="Back", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",12),command=lambda:showFrame(Frame5))
    btn1.place(relx=0.01, rely=0.05, relwidth=0.15, relheight=0.06)