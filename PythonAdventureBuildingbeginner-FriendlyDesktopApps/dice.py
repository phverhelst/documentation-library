import tkinter as tk
import random

root = tk.Tk()

root.title("Dice Roller")
root.geometry("500x300")
root.configure(background="white")

number_generated = tk.StringVar()
number_generated.set("1 to 6")

label = tk.Label(
    root,
    textvariable= number_generated,
    background="white",
    foreground="#DD571C",
    font=("Helvetica", 60),
    pady= 30
)
label.pack()

def roll():
    print("Rolling")
    number_generated.set(str(random.randint(1, 6)))


button = tk.Button(
    root,
    text = "Roll",
    command = roll,
    bg="#DD571C",
    fg="#DD571C",
    activebackground="#DD571C",
    activeforeground="white",
    highlightbackground="#DD571C",
    highlightcolor="white",
    font=("Helvetica", 60)
    
    )
button.pack()

root.mainloop()