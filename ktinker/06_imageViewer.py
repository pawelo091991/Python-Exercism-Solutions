from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to Code at Codemy.com')
root.iconbitmap("05_workspace.ico")

my_img = ImageTk.PhotoImage(Image.open("06_images/stockphoto.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("06_images/stockphoto1.jpg"))
my_img3 = ImageTk.PhotoImage(Image.open("06_images/stockphoto2.jpg"))

image_list = [my_img, my_img2, my_img3]

my_label = Label(image=my_img)
my_label.grid(row=0, column=0, columnspan=3)

button_back = Button(root, text="<<")
button_exit = Button(root, text="EXIT PROGRAM", command=root.quit)
button_foward = Button(root, text=">>")

button_back.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
button_foward.grid(row=1, column=2)

root.mainloop()