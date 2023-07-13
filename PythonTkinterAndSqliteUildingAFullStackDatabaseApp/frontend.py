import tkinter as tk
from tkinter import *

root = Tk()
root.title("Online School")
root.geometry("800x300")


name = Label(root, text = "Course Name", padx=10, pady = 20, font=("Helvetica", 20))
name.grid(row = 0, column = 0)

name_text = StringVar()
name_entry = Entry(root, textvariable = name_text)
name_entry.grid(row = 0, column=1)



category = Label(root, text="Category", padx=10,  pady = 20, font=("Helvetica", 20))
category.grid(row = 1, column = 0)

category_text = StringVar()
category_entry = Entry(root, textvariable = name_text)
category_entry.grid(row = 1, column=1)



author = Label(root, text="Author", padx=10,  pady = 20, font=("Helvetica", 20))
author.grid(row = 0, column = 2)

author_text = StringVar()
author_entry = Entry(root, textvariable = name_text)
author_entry.grid(row = 0, column=3)





price = Label(root, text="Price", padx=10,  pady = 20, font=("Helvetica", 20))
price.grid(row = 1, column = 2)

price_text = StringVar()
price_entry = Entry(root, textvariable = name_text)
price_entry.grid(row = 1, column=3)



root.mainloop()