from tkinter import *

root = Tk()
root.title("Form")
root.geometry("500x350")


fields = "First name", "last Name", "Course Name", "City"

def build_form(root, fields):
    entries = []
    for field in fields:
        frame = Frame(root)
        frame.pack(side = TOP)

        entry = Entry(frame)
        entry.pack(side = RIGHT)       

        entries.append((field, entry))

        label = Label(
            frame,
            text = field,
            pady=20,
            font = ("Helevetica", 20)
            )
        label.pack(side = LEFT)
    return entries



entries = build_form(root, fields)

def print_form(entries):
    for entry in entries:
        print("%s:%s"%(entry[0], entry[1].get()))


button = Button(
    root,
    text = "print",
    command = (lambda e = entries : print_form(entries)),
    font = ("Helevetica", 20)
    )
button.pack()




root.mainloop()