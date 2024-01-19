import sqlite3
from tkinter import messagebox
from Frames.viewSuggestion import *
from tkinter import *
from PIL import ImageTk,Image


def AddSuggestion(Frame3,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame7,Frame5):

    def missingPopUp():
        messagebox.showerror(title='Missing Parameters', message = 'You Entered Missing Parameters')

    def successPopUp():
        messagebox.showinfo(title=None,message='Successfully Recorded your Suggestion')

    def submitSuggestionInfo():
        conn=sqlite3.connect("Library.db")
        c = conn.cursor()

        if bookName.get() == '' or bookAuthor.get() == '' or yourName.get() == '':
            missingPopUp()
        else:
            c.execute("INSERT INTO suggestions VALUES (:1, :2, :3)",
                        {
                            '1': bookName.get(),
                            '2': yourName.get(),
                            '3': bookAuthor.get(),
                        })
            
            conn.commit()

            conn.close()

            successPopUp()

            yourName.delete(0, END)
            bookName.delete(0, END)
            bookAuthor.delete(0, END)

            
            viewSuggestions(Frame7,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5)


    Canvas3 = Canvas(Frame3,width=1100,height=650)

    Canvas3.create_image(0, 0, image=img,anchor= "nw")
    Canvas3.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas3.pack(expand=True, fill="both")

    Canvas3.config(bg="white")
    Canvas3.pack(expand=True, fill=BOTH)

    headingFrame1 = Frame(Frame3, bg="#3D2B1F", bd=5)
    headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    headingLabel = Label(headingFrame1, text="Suggest a Book to the Library", bg='#d8b785', fg='#3D2B1F', font=('Monotype Corsiva', 26))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(Frame3, bg='#3D2B1F')
    labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    # Book Name
    lb1 = Label(labelFrame, text="Enter your name : ", bg='#3D2B1F', fg='#d8b785',font=("Cooper Black",13))
    lb1.place(relx=0.05, rely=0.3, relheight=0.08)

    yourName = Entry(labelFrame,bg="#d8b785",font=("Cooper Black",12),fg="#3D2B1F")
    yourName.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.1)

    # Book Author
    lb2 = Label(labelFrame, text="Book Name             : ", bg='#3D2B1F', fg='#d8b785',font=("Cooper Black",13))
    lb2.place(relx=0.05, rely=0.45, relheight=0.08)

    bookName = Entry(labelFrame,bg="#d8b785",font=("Cooper Black",12),fg="#3D2B1F")
    bookName.place(relx=0.3, rely=0.45, relwidth=0.62, relheight=0.1)

    # Book Date
    lb3 = Label(labelFrame, text="Book Author          : ", bg='#3D2B1F', fg='#d8b785',font=("Cooper Black",12))
    lb3.place(relx=0.05, rely=0.60, relheight=0.08)

    bookAuthor = Entry(labelFrame,bg="#d8b785",font=("Cooper Black",12),fg="#3D2B1F")
    bookAuthor.place(relx=0.3, rely=0.60, relwidth=0.62, relheight=0.1)

    submit = Button(Frame3,text="SUGGEST BOOK",bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",12), command=submitSuggestionInfo)
    submit.place(relx=0.65, rely=0.68, relwidth=0.17, relheight=0.07)

    # goBack = Button(root,text="Back", command=lambda:showFrame(Frame1))
    goBack = Button(Frame3,text="BACK",bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",12),command=lambda:showFrame(Frame1))
    goBack.place(relx=0.35, rely=0.68, relwidth=0.17, relheight=0.07)





    # Canvas3 = Canvas(Frame3,width=1100,height=650)

    # Canvas3.create_image(0, 0, image=img,anchor= "nw")
    # Canvas3.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    # Canvas3.pack(expand=True, fill="both")

    # Canvas3.config(bg="white")
    # Canvas3.pack(expand=True, fill=BOTH)

    # headingFrame1 = Frame(Frame3, bg="#FFBB00", bd=5)
    # headingFrame1.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.13)

    # headingLabel = Label(headingFrame1, text="Suggest a Book to the Library", bg='black', fg='white', font=('Courier', 15))
    # headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    # labelFrame = Frame(Frame3, bg='black')
    # labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.6)

    # # Book Name
    # lb1 = Label(labelFrame, text="Enter you name : ", bg='black', fg='white')
    # lb1.place(relx=0.05, rely=0.1, relheight=0.08)

    # yourName = Entry(labelFrame)
    # yourName.place(relx=0.3, rely=0.1, relwidth=0.62, relheight=0.08)

    # # Book Author
    # lb2 = Label(labelFrame, text="Book Name : ", bg='black', fg='white')
    # lb2.place(relx=0.05, rely=0.2, relheight=0.08)

    # bookName = Entry(labelFrame)
    # bookName.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # # Book Date
    # lb3 = Label(labelFrame, text="Book Author : ", bg='black', fg='white')
    # lb3.place(relx=0.05, rely=0.3, relheight=0.08)

    # bookAuthor = Entry(labelFrame)
    # bookAuthor.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # submit = Button(Frame3,text="Suggest book", command=submitSuggestionInfo)
    # submit.place(relx=0.6, rely=0.81, relwidth=0.1, relheight=0.08)

    # # goBack = Button(root,text="Back", command=lambda:showFrame(Frame1))
    # goBack = Button(Frame3,text="Back",command=lambda:showFrame(Frame1))
    # goBack.place(relx=0.3, rely=0.81, relwidth=0.1, relheight=0.08)
