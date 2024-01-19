import sqlite3
from Frames.BookInfo import *
from tkinter import *
from tkinter import ttk

def viewBooks(Frame6,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame8):

    def OnDoubleClick(event):
        item = str(libTree.selection())
        transitionString = item.replace('(\''," ")
        removeSpace = transitionString.replace('\',)',' ')
        myString = removeSpace.strip()
        rowID = (int(myString)+1)
        
        showFrame(Frame8)
        BookInfo(Frame8,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame6,rowID)
            
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
        for item in libTree.get_children():
            libTree.delete(item)
        # Insert into treeview
        for item in LibItems:
            genres = item[4] + ', ' + item[5] + ', ' + item[6]
            libTree.insert(parent='', index='end', iid=item[0] - 1, text="",
                        values=(item[0], item[1], item[2], item[3], genres))

        libTree.bind("<Double-1>", OnDoubleClick)
    
    
    Canvas1 = Canvas(Frame6,width=1100,height=650)

    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    #Treeview frame
    tree_frame = Frame(Frame6)
    tree_frame.place(relx=0.05,rely=0.15, relwidth=0.9, relheight=0.8)



    style = ttk.Style()
    style.theme_use("clam")

    style.configure("Treeview",
                    background = "#d8b785",
                    foreground = "#3D2B1F",
                    rowheight  = 30,
                    font =("Arial Black",10),
                    fieldbackground = "#d8b785"
                    )
    #Initialize treeview
    libTree = ttk.Treeview(tree_frame)



    style.map('Treeview',
              background = [('selected','#3D2B1F')]
              )


    #Place
    libTree.place(relx=0,rely=0, relwidth=1, relheight=1)

    #Treeview scrollbar
    tree_scroll = Scrollbar(tree_frame, orient='vertical', command=libTree.yview)
    tree_scroll.pack(side=RIGHT, fill=Y)

    tree_Scrollx = Scrollbar(tree_frame,orient='horizontal',command=libTree.xview)
    tree_Scrollx.pack(side=BOTTOM,fill=X)

    libTree.configure(xscrollcommand=tree_Scrollx.set)
    libTree.configure(yscrollcommand=tree_scroll.set)


    #Define columns
    libTree['columns'] = ("ID", "Title", "Author", "Published", "Genres")

    #Format columns
    libTree.column("#0", width=0, stretch=NO)
    libTree.column("ID", anchor=W, width=30, minwidth=20, stretch=NO)
    libTree.column("Title", anchor=W, width=600, minwidth=20)
    libTree.column("Author", anchor=W, width=220, minwidth=20)
    libTree.column("Published", anchor=W, width=120, minwidth=20, stretch=NO)
    libTree.column("Genres", anchor=W, width=450, minwidth=20)

    #Create headings
    libTree.heading("#0", text="", anchor=W)
    libTree.heading("ID", text="ID", anchor=W)
    libTree.heading("Title", text="Title", anchor=W)
    libTree.heading("Author", text="Author", anchor=W)
    libTree.heading("Published", text="Published", anchor=W)
    libTree.heading("Genres", text="Genres", anchor=W)

    libTree.bind('<Motion>', 'break')
    libTree.bind("<Double-1>", OnDoubleClick)


    
    #Search bar
    searchBar = Entry(Frame6, bg="#d8b785",bd=2,font=('Constantia',12))
    searchBar.place(relx=0.25, rely=0.04, relwidth=0.5,relheight=0.05)

    #Search Button
    searchBtn = Button(Frame6, text="Search", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",10), command=lambda:libInject(libFetch(searchBar.get())))
    searchBtn.place(relx=0.45, rely=0.1, relwidth=0.1)

    libInject(libFetch(''))

    btn1 = Button(Frame6, text="BACK", bg='#d8b785', fg='#3D2B1F',font=("Cooper Black",12),command=lambda:showFrame(Frame1))
    btn1.place(relx=0.01, rely=0.05, relwidth=0.15, relheight=0.06)