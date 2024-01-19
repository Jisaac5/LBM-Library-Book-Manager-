import sqlite3
from tkinter import messagebox
from Frames.BorrowReturn import borrowReturn
from Frames.viewBooks import *
from tkinter import *

from Frames.viewDelete import viewDelete





def AddBook(Frame2,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5,Frame6,Frame1,img2,Frame8,Frame9,Frame10):

    def missingPopUp():
        messagebox.showerror(title='Missing Parameters', message = 'You Entered Missing Parameters')

    def successPopUp():
        messagebox.showinfo(title=None,message='Successfully Added Book to the Library')


    def submitBookInfo():
        conn=sqlite3.connect("Library.db")
        c = conn.cursor()

        if bookInfo1.get() == '' or bookInfo2.get() == '' or bookInfo3.get() == '' or bookInfo4a.get() == '' or bookInfo4b.get() == '' or bookInfo4c.get() == '' or bookInfo5.get(1.0, END) == '':
            missingPopUp()
        else:
            c.execute("INSERT INTO books VALUES (:1, :2, :3, :4, :5, :6, :7, :8)",
                        {
                            '1': bookInfo1.get(),
                            '2': bookInfo2.get(),
                            '3': bookInfo3.get(),
                            '4': bookInfo4a.get(),
                            '5': bookInfo4b.get(),
                            '6': bookInfo4c.get(),
                            '7': "available",
                            '8': bookInfo5.get(1.0,END)
                        })
            
            conn.commit()
            conn.close()

            successPopUp()

            bookInfo1.delete(0, END)
            bookInfo2.delete(0, END)
            bookInfo3.delete(0, END)
            bookInfo4a.delete(0, END)
            bookInfo4b.delete(0, END)
            bookInfo4c.delete(0, END)
            bookInfo5.delete(1.0, END)

            
            viewBooks(Frame6,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame8)
            viewDelete(Frame9,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5,Frame6,Frame1,Frame8,Frame10)
            borrowReturn(Frame10,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1)
            


    Canvas2 = Canvas(Frame2)

    Canvas2.create_image(0, 0, image=img2,anchor= "nw")
    Canvas2.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas2.pack(expand=True, fill="both")

    headingFrame1 = Frame(Frame2, bg="#3D2B1F", bd=3)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Add Books", bg="#d8b785", fg='#3D2B1F', font=('Monotype Corsiva', 26))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    headingFrame1 = Frame(Frame2, bg="#3D2B1F", bd=3)
    headingFrame1.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.78)
    labelFrame = Frame(Frame2, bg="#3D2B1F")
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.7)



    # Book Name
    lb1 = Label(labelFrame, text="Book Name : ", bg="#3D2B1F", fg='#d8b785',font=("Cooper Black",12),)
    lb1.place(relx=0.05, rely=0.1, relheight=0.08)

    bookInfo1 = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo1.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # Book Author
    lb2 = Label(labelFrame, text="Book Author : ", bg="#3D2B1F", fg='#d8b785',font=("Cooper Black",12),)
    lb2.place(relx=0.05, rely=0.2, relheight=0.08)

    bookInfo2 = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo2.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Book Date
    lb3 = Label(labelFrame, text="Book Date Published : ", bg="#3D2B1F", fg='#d8b785',font=("Cooper Black",12),)
    lb3.place(relx=0.05, rely=0.3, relheight=0.08)

    bookInfo3 = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo3.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # Book Genre
    lb4 = Label(labelFrame, text="Book Genres : ", bg="#3D2B1F",fg="#d8b785",font=("Cooper Black",12),)
    lb4.place(relx=0.05, rely=0.4, relheight=0.08)

    bookInfo4a = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo4a.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)
    # text="                           : ", 
    dot1 = Label(labelFrame, bg="#3D2B1F",fg="#d8b785",font=("Cooper Black",12),)
    dot1.place(relx=0.05, rely=0.5, relheight=0.08)
    bookInfo4b = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo4b.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    dot2 = Label(labelFrame, bg="#3D2B1F", fg="#d8b785", font=("Cooper Black", 12), )
    dot2.place(relx=0.05, rely=0.6, relheight=0.08)
    bookInfo4c = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo4c.place(relx=0.3, rely=0.6, relwidth=0.62, relheight=0.08)

    # Book Synopsis
    lb5 = Label(labelFrame, text="Synopsis : ", bg='#3D2B1F', fg='#d8b785',font=("Cooper Black",12),)
    lb5.place(relx=0.05, rely=0.7, relheight=0.08)

    bookInfo5 = Text(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    bookInfo5.place(relx=0.3, rely=0.7, relwidth=0.62, relheight=0.2)

    submit = Button(Frame2,text="ADD BOOK",bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10), command=submitBookInfo)
    submit.place(relx=0.65, rely=0.88, relwidth=0.13, relheight=0.08)

    goBack = Button(Frame2,text="BACK",bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10), command=lambda:showFrame(Frame5))
    goBack.place(relx=0.35, rely=0.88, relwidth=0.13, relheight=0.08)