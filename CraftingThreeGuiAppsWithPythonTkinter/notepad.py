import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from tkinter import *
from tkinter import filedialog, messagebox


root  = tk.Tk()


root.title("Notes")

textarea = ScrolledText(root)
textarea.pack()

menu = Menu(root)
file = Menu(menu, tearoff = 0)

def Open():
    root.filename = filedialog.askopenfilename(
        initialdir = "/",
        title = "Select File",
        filetypes = (
            ("txt files", "*.txt"),
            ("all files", "*.*")
            )
        )
    file = open(root.filename)
    text.insert("end", file.read())

def  Save():
    pass

def SaveAs():
    root.filename = filedialog.asksaveasfile(
        mode = "w",
        defaultextension = ".txt"
    )
    if root.filename is None:
        return
    file_to_save = str(text.get  (1.0, END))
    root.filename.write(file_to_save)
    root.filename.close()

def Exit():
    message = messagebox.askquestion("Notepad", "Do you want to save?")
    if message == "yes":
        SaveAs()
    else:
        root.destroy()



file.add_command(label = "Open", command = Open)
file.add_command(label = "Save", command = Save)
file.add_command(label = "Save As", command = SaveAs)
file.add_separator()
file.add_command(label = "Exit", command = Exit)

menu.add_cascade(label = "File", menu = file)


root.config(menu = menu)



root.mainloop()