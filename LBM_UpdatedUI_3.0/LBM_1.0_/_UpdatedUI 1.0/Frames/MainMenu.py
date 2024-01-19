from tkinter import *
from Frames.AdminLogin import *
from Frames.viewBooks import *
from Frames.viewBooks import *


def MainMenu(mainMenuFrame,img,newImageSizeWidth,newImageSizeHeight,showFrame,root,viewBookFrame,suggestFrame,AdminLoginFrame, brFrame): 

    def viewBookCommand():
        showFrame(viewBookFrame)

    Canvas1 = Canvas(mainMenuFrame,width=1100,height=650)

    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    mainMenuFrameBorder1 = Frame(mainMenuFrame, bg="#3D2B1F", bd=3)
    mainMenuFrameBorder1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(mainMenuFrameBorder1, text="LBM", bg="#d8b785",fg="#3D2B1F",
                        font=('Monotype Corsiva', 32))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    mainMenuFrameBorder1 = Frame(mainMenuFrame, bg="#3D2B1F", bd=3)
    mainMenuFrameBorder1.place(relx=0.29, rely=0.32, relwidth=0.41, relheight=0.65)

    btn1 = Button(mainMenuFrame, text="VIEW BOOKS", fg='#3D2B1F',font=("Poppins",18),bg="#d8b785",activebackground="#f4d6a2",command=viewBookCommand)
    btn1.place(relx=0.32, rely=0.36, relwidth=0.35, relheight=0.1)

    btn2 = Button(mainMenuFrame, text="BORROW/RETURN", fg='#3D2B1F',font=("Poppins",18),bg="#d8b785",activebackground="#f4d6a2", command=lambda:showFrame(brFrame))
    btn2.place(relx=0.32, rely=0.48, relwidth=0.35, relheight=0.1)

    btn3 = Button(mainMenuFrame, text="SUGGEST A BOOK",  fg='#3D2B1F',font=("Poppins",18),bg="#d8b785", activebackground="#f4d6a2",command=lambda:showFrame(suggestFrame))
    btn3.place(relx=0.32, rely=0.60, relwidth=0.35, relheight=0.1)

    btn4 = Button(mainMenuFrame, text="ADMIN COMMANDS",  fg='#3D2B1F',font=("Poppins",18),bg="#d8b785", activebackground="#f4d6a2",command=lambda:showFrame(AdminLoginFrame))
    btn4.place(relx=0.32, rely=0.72, relwidth=0.35, relheight=0.1)

    btn5 = Button(mainMenuFrame, text="EXIT",  fg='#3D2B1F',font=("Poppins",18),bg="#d8b785",activebackground="#f4d6a2",command=root.quit)
    btn5.place(relx=0.32, rely=0.84, relwidth=0.35, relheight=0.1)
















    # Canvas1 = Canvas(mainMenuFrame,width=1100,height=650)

    # Canvas1.create_image(0, 0, image=img,anchor= "nw")
    # Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    # Canvas1.pack(expand=True, fill="both")

    # mainMenuFrameBorder1 = Frame(mainMenuFrame, bg="#FFBB00", bd=3)
    # mainMenuFrameBorder1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    # headingLabel = Label(mainMenuFrameBorder1, text="Library Management System", bg='black', fg='white',
    #                     font=('Courier', 15))
    # headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    # btn1 = Button(mainMenuFrame, text="VIEW BOOKS", fg='black',font=("Arial",12),command=viewBookCommand)
    # btn1.place(relx=0.32, rely=0.4, relwidth=0.35, relheight=0.1)

    # btn2 = Button(mainMenuFrame, text="BORROW/RETURN", fg='black',font=("Arial",12))
    # btn2.place(relx=0.32, rely=0.5, relwidth=0.35, relheight=0.1)

    # btn3 = Button(mainMenuFrame, text="SUGGEST A BOOK",  fg='black',font=("Arial",12), command=lambda:showFrame(suggestFrame))
    # btn3.place(relx=0.32, rely=0.6, relwidth=0.35, relheight=0.1)

    # btn4 = Button(mainMenuFrame, text="ADMIN COMMANDS",  fg='black',font=("Arial",12), command=lambda:showFrame(AdminLoginFrame))
    # btn4.place(relx=0.32, rely=0.7, relwidth=0.35, relheight=0.1)

    # btn5 = Button(mainMenuFrame, text="EXIT",  fg='black',font=("Arial",12),command=root.quit)
    # btn5.place(relx=0.32, rely=0.8, relwidth=0.35, relheight=0.1)
