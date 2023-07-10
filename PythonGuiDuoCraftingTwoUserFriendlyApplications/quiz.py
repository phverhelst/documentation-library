import tkinter as tk
import load_questions


class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("900x400")
        self.current_question_index =0
        self.build_gui()
        self.root.mainloop()
        

    def start(self):

        self.start_button.pack_forget()
        self.questions = load_questions.get_questions("PythonGuiDuoCraftingTwoUserFriendlyApplications\questions.csv")
        current_question = self.get_question()
        self.questions_label.config(text=current_question + "?")

        options = self.questions[self.current_question_index][1:len(self.questions) + 2]
        for option, index in zip(options, range(len(options))):
            self.option_buttons.append(tk.Radiobutton(
                self.questions_container,
                text= option,
                value= index + 1,
                variable= self.user_answer
            ))
            self.option_buttons[-1].pack()


    def get_question(self):
        return self.questions[self.current_question_index][0]

    def  get_options(self):
        return self.questions[self.current_question_index][1:len(self.questions) +2]

    def check_answer(self):
        if str(self.user_answer.get()) ==self.questions[self.current_question_index][-1]:
            self.score.set(self.score.get() + 1)



    def show_next(self):
        if (self.current_question_index < len(self.questions)):
            self.check_answer()
        
        self.current_question_index += 1
        if (self.current_question_index < len(self.questions)):
            next_question = self.get_question()
            self.questions_label.config(text= next_question + "?")
        
            next_options = self.get_options()
            for option_button, option, index in zip(self.option_buttons, next_options, range(len(next_options))):
                option_button.config(text = option, value = index + 1)
    
    def build_gui(self):

        self.questions_container = tk.Frame(self.root)
        self.questions_container.pack()

        self.questions_label = tk.Label(
            self.questions_container,
            text="Questions",
            font = ("Helvetica", 20),
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

        self.option_buttons = []
        self.user_answer = tk.IntVar()

        self.score = tk.IntVar()
        self.score.set(0)
        self.score_label = tk.Label(
            self.root,
            textvariable= str(self.score),
            font = ("Helvetica", 40),
            pady=30
            )
        self.score_label.pack()





if __name__ == "__main__":
    App()