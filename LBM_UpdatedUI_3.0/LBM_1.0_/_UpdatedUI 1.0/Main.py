from Frames.AddSuggestion import*
from Frames.viewDelete import*
from Frames.AddBook import*
from Frames.MainMenu import*
from Frames.AdminLogin import*
from Frames.BookInfo import*
from Frames.viewBooks import*
from Frames.AdminMenu import*
from Frames.viewSuggestion import*
from Frames.BorrowReturn import*
from tkinter import *
from PIL import ImageTk,Image


#Frame Switch Function
def showFrame(frame):
    frame.tkraise()

#Formatting Window
root = Tk()

root.title("Library Management System")
root.resizable(False, False)

window_width = 960 
window_height = 540

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

#Formating Background
#bg image size multiplier
same = True
n = 1.8
#background image
background_image = Image.open("images\mainbg.jpg")
[imageSizeWidth, imageSizeHeight] = background_image.size

newImageSizeWidth = int(imageSizeWidth * n)
if same:
    newImageSizeHeight = int(imageSizeHeight * n)
else:
    newImageSizeHeight = int(imageSizeHeight / n)

background_image = background_image.resize((newImageSizeWidth, newImageSizeHeight), Image.ANTIALIAS)
img = ImageTk.PhotoImage(background_image)

n2 = .3

background_image2 = Image.open("images/adminbg.jpg")
[imageSizeWidth2, imageSizeHeight2] = background_image2.size

newImageSizeWidth2 = int(imageSizeWidth2 * n2)
if same:
    newImageSizeHeight2 = int(imageSizeHeight2 * n2)
else:
    newImageSizeHeight2 = int(imageSizeHeight2 / n2)

background_image2 = background_image2.resize((newImageSizeWidth2, newImageSizeHeight2), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(background_image2)

#FRAMES DEFINED

Frame1 = Frame(root) #MAIN MENU

Frame2 = Frame(root) #ADD BOOKS

Frame3 = Frame(root) #ADD SUGGESTIONS

Frame4 = Frame(root) #Admin Controls

Frame5 = Frame(root) #ADMIN MENU

Frame6 = Frame(root) #VIEWBOOKS 

Frame7 = Frame(root) #VIEW SUGGESTIONS

Frame8 = Frame(root) #Book Info Menu

Frame9 = Frame(root) #ADD DELETE MENU

Frame10 = Frame(root) #BORROW RETURN MENU

##MAIN MENU FRAME

MainMenu(Frame1,img,newImageSizeWidth,newImageSizeHeight,showFrame,root,Frame6,Frame3,Frame4,Frame10)

##ADD BOOK FRAME

AddBook(Frame2,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5,Frame6,Frame1,img2,Frame8,Frame9,Frame10)

##SUGGESTION FRAME

AddSuggestion(Frame3,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame7,Frame5)

#ADMIN LOGIN FRAME

AdminLogin(Frame4,img2,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame5)

#ADMIN MENU FRAME

AdminMenu(Frame5,img2,newImageSizeWidth,newImageSizeHeight,Frame2,showFrame,Frame1,Frame7,Frame9)

#VIEW BOOKS FRAME

viewBooks(Frame6,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1,Frame8)

#VIEW SUGGESTION FRAME

viewSuggestions(Frame7,img2,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5)

#BOOK INFO FRAME

BookInfo(Frame8,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame6,6)

#VIEW DELETE FRAME

viewDelete(Frame9,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame5,Frame6,Frame1,Frame8,Frame10)

#BORROW RETURN

borrowReturn(Frame10,img,newImageSizeWidth,newImageSizeHeight,showFrame,Frame1)

#FRAME CYCLE LOOP

for frame in (Frame1,Frame2,Frame3,Frame4,Frame5,Frame6,Frame7,Frame8,Frame9,Frame10):
    frame.place(relwidth=1, relheight=1)

##DEFAULT FRAME

showFrame(Frame1)

root.mainloop()