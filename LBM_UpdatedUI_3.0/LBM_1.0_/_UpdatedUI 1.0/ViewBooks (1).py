from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
import sqlite3
# from dbAction import view, viewSpecific


root = Tk()

root.title("Library")
root.resizable(False, False)

window_height = 650
window_width = 1100

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

x_cordinate = int((screen_width/2) - (window_width/2))
y_cordinate = int((screen_height/2) - (window_height/2))

root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

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

Canvas1 = Canvas(root,width=1100,height=650)

Canvas1.create_image(0, 0, image=img,anchor= "nw")
Canvas1.config(bg="white", width=newImageSizeWidth, height=newImageSizeHeight)
Canvas1.pack(expand=True, fill="both")

searchWindowLabel = Label()

# Treeview frame
tree_frame = Frame(root)
tree_frame.place(relx=0.05, rely=0.15, relwidth=0.9, relheight=0.75)

# Treeview scrollbar
tree_scroll = Scrollbar(tree_frame)
tree_scroll.pack(side=RIGHT, fill=Y)

# Initialize treeview
libTree = ttk.Treeview(tree_frame, yscrollcommand=tree_scroll.set)
tree_scroll.config(command=libTree.yview)

# Place
libTree.place(relx=0, rely=0, relwidth=1, relheight=1)

# Define columns
libTree['columns'] = ("ID", "Title", "Author", "Published", "Genres")

# Format columns
libTree.column("#0", width=0, stretch=NO)
libTree.column("ID", anchor=W, width=20, minwidth=20, stretch=NO)
libTree.column("Title", anchor=W, width=100, minwidth=20)
libTree.column("Author", anchor=W, width=30, minwidth=20)
libTree.column("Published", anchor=W, width=65, minwidth=20, stretch=NO)
libTree.column("Genres", anchor=W, width=80, minwidth=20)

# Create headings
libTree.heading("#0", text="", anchor=W)
libTree.heading("ID", text="ID", anchor=W, command=lambda:sortDef('rowid'))
libTree.heading("Title", text="Title", anchor=W, command=lambda:sortDef('name'))
libTree.heading("Author", text="Author", anchor=W, command=lambda:sortDef('author'))
libTree.heading("Published", text="Published", anchor=W, command=lambda:sortDef('date'))
libTree.heading("Genres", text="Genres", anchor=W, command=lambda:sortDef('genre1'))

#Search bar
searchBar = Entry(root, bg="white")
searchBar.place(relx=0.25, rely=0.045, relwidth=0.5)

#Search Button
searchBtn = Button(root, text="Search", bg='white', command=lambda:libInject(libFetch(searchBar.get())))
searchBtn.place(relx=0.475, rely=0.1, relwidth=0.05)


def sortDef(sortFilter):
    print('test')



def libFetch(searchKeyword):
    # Fetch data from db
    dbconn = sqlite3.connect("Library.db")
    dbcursor = dbconn.cursor()

    dbcursor.execute("SELECT rowid, * FROM books WHERE name LIKE '%{}%'".format(searchKeyword))
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


libInject(libFetch(''))



root.mainloop()