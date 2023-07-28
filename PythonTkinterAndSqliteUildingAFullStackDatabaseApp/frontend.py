import tkinter as tk
from tkinter import *
import backend

root = Tk()
root.title("Online School")
root.geometry("1000x500")


name = Label(root, text = "Course Name", padx=10, pady = 20, font=("Helvetica", 20))
name.grid(row = 0, column = 0)

name_text = StringVar()
name_entry = Entry(root, textvariable = name_text)
name_entry.grid(row = 0, column=1)



category = Label(root, text="Category", padx=10,  pady = 20, font=("Helvetica", 20))
category.grid(row = 1, column = 0)

category_text = StringVar()
category_entry = Entry(root, textvariable = category_text)
category_entry.grid(row = 1, column=1)



author = Label(root, text="Author", padx=10,  pady = 20, font=("Helvetica", 20))
author.grid(row = 0, column = 2)

author_text = StringVar()
author_entry = Entry(root, textvariable = author_text)
author_entry.grid(row = 0, column=3)





price = Label(root, text="Price", padx=10,  pady = 20, font=("Helvetica", 20))
price.grid(row = 1, column = 2)

price_text = StringVar()
price_entry = Entry(root, textvariable = price_text)
price_entry.grid(row = 1, column=3)

def get_selected_row(event):
    global get_selected_row
    index = listbox.curselection()[0]
    selected_row = listbox.get(index)
    print(get_selected_row)

listbox = Listbox(root, height=10, width=60)
listbox.grid(row = 2, column=0, rowspan=4, columnspan=2)
listbox.bind("<<ListBoxSelect>>", get_selected_row)

def create_entry():
    backend.create(name_text.get(), category_text.get(), author_text.get(), price_text.get())
    listbox.delete(0, END)
    listbox.insert(END, (name_text.get(), category_text.get(), author_text.get(), price_text.get()))

create_entry_button = Button(root, text="Create Course", font=("Helvetica", 30), command = create_entry)
create_entry_button.grid(row = 4, column = 3)


def read_all():
    listbox.delete(0, END)
    for row in backend.read_all():
        listbox.insert(END, row)



read_all_button = Button(root, text="Show All Courses", font=("Helvetica", 30), command = read_all)
read_all_button.grid(row = 5, column=3)

root.mainloop()