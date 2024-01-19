from tkinter import*
import sqlite3


def BookInfo(Frame8,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame6,rowNumber):
    def fetchInformation():
        conn = sqlite3.connect('Library.db')
        c = conn.cursor()

        c.execute("SELECT rowid, * FROM books where rowid={}" .format(rowNumber))

        item = c.fetchone()

        conn.commit()
        conn.close()

        return item

    Canvas3 = Canvas(Frame8,width=1100,height=650)

    Canvas3.create_image(0, 0, image=img,anchor= "nw")
    Canvas3.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas3.pack(expand=True, fill="both")

    Canvas3.config(bg="white")
    Canvas3.pack(expand=True, fill=BOTH)

    item = fetchInformation()

    bookName = str(item[1])
    bookAuthor = ("A book by " + item[2])
    datePublished = str(item [3])
    bookGenre1 = item[4]
    bookGenre2 = item[5]
    bookGenre3 = item[6]
    status = item[7]
    synopsis = item[8]

    headingFrame1 = Frame(Frame8, bg="#3D2B1F", bd=5)
    headingFrame1.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.13, anchor=CENTER)

    headingFrame2 = Frame(Frame8, bg="#3D2B1F", bd=5)
    headingFrame2.place(relx=0.5, rely=0.32, relwidth=0.43, relheight=0.30, anchor=CENTER)

    headingLabel = Label(headingFrame1, text=bookName, bg='#d8b785', fg='#3D2B1F', font=('Monotype Corsiva',18), wraplength=450)
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    authorLabel = Label(Frame8, text=bookAuthor, bg='#3D2B1F', fg='#d8b785', font=("Cooper Black",12), wraplength=450)
    authorLabel.place(relx=.5, rely=.23, relwidth=.4, relheight=0.1, anchor=CENTER)

    genresLabel = Label(Frame8, text=(bookGenre1 + ', ' + bookGenre2 + ', ' + bookGenre3), bg='#3D2B1F', fg='#d8b785', font=("Cooper Black",12), wraplength=450)
    genresLabel.place(relx=.5, rely=.29, relwidth=.4, relheight=.05, anchor=CENTER)

    dateLabel = Label(Frame8, text=('Published in ' + datePublished), bg='#3D2B1F', fg='#d8b785', font=("Cooper Black",12), wraplength=450)
    dateLabel.place(relx=.5, rely=.36, relwidth=.4, relheight=.08, anchor=CENTER)

    statusLabel = Label(Frame8, text=('status: ' + status), bg='#3D2B1F', fg='#d8b785', font=("Cooper Black",12), wraplength=450)
    statusLabel.place(relx=.5, rely=.42, relwidth=.4, relheight=.02, anchor=CENTER)

    synopsisLabel = Label(Frame8, text="SYNOPSIS", bg='#3D2B1F', fg='#d8b785', font=("Cooper Black",12), wraplength=450)
    synopsisLabel.place(relx=.5, rely=.54, relwidth=.4, relheight=.08, anchor=CENTER)

    synopsisFrame = Frame(Frame8,bg='#3D2B1F', bd=5)
    synopsisFrame.place(anchor=CENTER, relx=.5, rely=.77,relwidth=.85,relheight=.4)

    synopsisBox = Text(synopsisFrame,font=('Constantia',13), fg="#3D2B1F",bg="#d8b785",wrap=WORD)
    synopsisBox.insert('1.0', synopsis)
    synopsisBox.config(state=DISABLED)
    synopsisBox.tag_configure("center", justify='center')
    synopsisBox.tag_add("center", 1.0, "end")
    synopsisBox.place(relx=0, rely=0, relwidth=.98,relheight=1)

    scroll = Scrollbar(synopsisFrame, orient='vertical', command=synopsisBox.yview)
    scroll.pack(side=RIGHT, fill=Y)

    synopsisBox.configure(yscrollcommand=scroll.set)

    goBack = Button(Frame8,text="BACK",command=lambda:showFrame(Frame6), fg='#3D2B1F', bg='#d8b785', font=('Cooper Black', 12))
    goBack.place(relx=0.1, rely=0.1, relwidth=0.15, relheight=0.06,anchor=CENTER)
