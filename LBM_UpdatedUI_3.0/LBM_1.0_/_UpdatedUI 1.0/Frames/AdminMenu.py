from tkinter import *


def AdminMenu(Frame5,img,newImageSizeWidth,newImageSizeHeight,Frame2,showFrame,Frame1,Frame7,Frame9):

    Canvas1 = Canvas(Frame5,width=1100,height=650)

    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    mainMenuFrameBorder1 = Frame(Frame5, bg="#3D2B1F", bd=3)
    mainMenuFrameBorder1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(mainMenuFrameBorder1, text="Administrator Controls", bg='#d8b785', fg='#3D2B1F',
                        font=('Monotype Corsiva', 26))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

    mainMenuFrameBorder1 = Frame(Frame5, bg="#3D2B1F", bd=3)
    mainMenuFrameBorder1.place(relx=0.29, rely=0.35, relwidth=0.411, relheight=0.55)

    btn1 = Button(Frame5, text="SHOW SUGGESTIONS", fg='#3D2B1F', bg='#d8b785',font=("Cooper Black",12),command=lambda:showFrame(Frame7))
    btn1.place(relx=0.32, rely=0.4, relwidth=0.35, relheight=0.1)

    btn2 = Button(Frame5, text="ADD BOOKS",  fg='#3D2B1F', bg='#d8b785', font=("Cooper Black",12),command=lambda:showFrame(Frame2))
    btn2.place(relx=0.32, rely=0.52, relwidth=0.35, relheight=0.1)

    btn3 = Button(Frame5, text="DELETE BOOKS", fg='#3D2B1F', bg='#d8b785', font=("Cooper Black",12),command=lambda:showFrame(Frame9))
    btn3.place(relx=0.32, rely=0.64, relwidth=0.35, relheight=0.1)

    btn4 = Button(Frame5, text="LOG OUT", fg='#3D2B1F', bg='#d8b785', font=("Cooper Black",12), command=lambda:showFrame(Frame1))
    btn4.place(relx=0.32, rely=0.76, relwidth=0.35,relheight=0.1)