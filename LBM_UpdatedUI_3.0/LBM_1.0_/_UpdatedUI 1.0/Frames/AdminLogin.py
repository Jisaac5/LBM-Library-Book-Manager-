from tkinter import *
from tkinter import messagebox

#Admin Page
def AdminLogin(Frame4,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame5):

    def missingPopUp():
        messagebox.showerror(title='Missing Parameters', message = 'Please Enter a Username and Password')
    def missingUsernamePopUp():
        messagebox.showerror(title='Missing Parameters', message = 'Please Enter a Username')
    def missingPasswordPopUp():
        messagebox.showerror(title='Missing Parameters', message = 'Please Enter a Password')
    def wrongCredentialsPopUp():
        messagebox.showerror(title='Incorrect Credentials', message = 'Username or Password Incorrect')

    def testCredentials():
        if Username.get() == 'admin' and Password.get() == 'admin':
            showFrame(Frame5)
            Username.delete(0, END)
            Password.delete(0, END)
        else:
            wrongCredentialsPopUp()

    def testInput():
        if Username.get() == '' and Password.get() == '':
            missingPopUp()
        elif Username.get() == '':
            missingUsernamePopUp()
        elif Password.get() == '':
            missingPasswordPopUp()
        else:
            testCredentials()
    Canvas1 = Canvas(Frame4,width=1100,height=650)

    Canvas1.create_image(0, 0, image=img,anchor= "nw")
    Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
    Canvas1.pack(expand=True, fill="both")

    mainMenuFrameBorder1 = Frame(Frame4, bg="#3D2B1F", bd=3)
    mainMenuFrameBorder1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

    headingLabel = Label(mainMenuFrameBorder1, text="Administrator Login", bg='#d8b785', fg='#3D2B1F',
                        font=('Monotype Corsiva', 26))
    headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)


    labelFrame = Frame(Frame4, bg='#3D2B1F')
    labelFrame.place(anchor = CENTER,relx=0.5, rely=0.5, relwidth=0.45, relheight=0.4)

    lb1 = Label(labelFrame, text="Username : ", fg='#d8b785', bg='#3D2B1F', font=("Cooper Black",12))
    lb1.place(relx=0.05, rely=0.2, relheight=.2)

    Username = Entry(labelFrame,bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    Username.place(relx=0.35, rely=0.25, relwidth=0.5, relheight=0.1)

    lb2 = Label(labelFrame, text="Password : ", fg='#d8b785', bg='#3D2B1F', font=("Cooper Black",12))
    lb2.place(relx=0.05, rely=0.4, relheight=0.2)

    Password = Entry(labelFrame,show='•',bg="#d8b785",fg="#3D2B1F",font=("Cooper Black",10))
    Password.place(relx=0.35, rely=0.45, relwidth=0.5, relheight=0.1)

    enter_btn = Button(labelFrame,text="BACK", bg="#d8b785", fg="#3D2B1F",font=("Cooper Black",10), command=lambda:showFrame(Frame1))
    enter_btn.place(relx=0.3, rely=0.8, relwidth=0.2, relheight=0.15)

    enter_btn = Button(labelFrame,text="ENTER",bg="#d8b785", fg="#3D2B1F",font=("Cooper Black",10),command = testInput)
    enter_btn.place(relx=0.6, rely=0.8, relwidth=0.2, relheight=0.15)







