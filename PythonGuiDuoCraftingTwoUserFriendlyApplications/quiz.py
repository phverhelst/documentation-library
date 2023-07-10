import tkinter as tk


class App:

    def start(self):
        print("Start")

    def show_next(self):
        print("Show Next")

    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.build_gui()
        self.root.mainloop()

    def build_gui(self):

        self.questions_container = tk.Frame(self.root)
        self.questions_container.pack()

        self.questions_label = tk.Label(
            self.questions_container,
            text="Questions",
            font = ("Helvetica", 40),
            pady=30
            )
        self.questions_label.pack()

        self.button_frame = tk.Frame(self.root)
        self.button_frame.pack()

        self.start_button = tk.Button(
            self.button_frame,
            text="Start",
            command = self.start,
            font = ("Helvetica", 40),
            pady=30
            )
        self.start_button.pack()

        self.next_button = tk.Button(
            self.button_frame,
            text="Next",
            command = self.show_next,
            font = ("Helvetica", 40),
            pady=30
            )
        self.next_button.pack()



if __name__ == "__main__":
    App()