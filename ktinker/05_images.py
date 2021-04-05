from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap("05_workspace.ico")

my_img = ImageTk.PhotoImage(Image.open("05_stockphoto.jpg"))
my_label = Label(image=my_img)
my_label.pack()


button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()