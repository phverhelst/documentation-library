import tkinter as tk
from tkinter.ttk import Notebook
import requests


class Translate(tk.Tk):

    def translate(self, target_language="es", text=None):
        if not text:
            text = self.english_entry.get(1.0, tk.END)

        url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl={}&tl{}&dt=t&q={}".format("en", "target_language", text)

        try:
            response = requests.get(url)
            response.raise_for_status()
            print(response.json())
        except Exception as e:
            print(e)


    def __init__(self):


        super().__init__()

        self.title("Translate")
        
        self.notebook = Notebook(self)
        self.notebook.pack(fill = tk.BOTH, expand = 1)

        english_tab = tk.Frame(self.notebook)
        self.english_entry = tk.Text(english_tab)
        self.english_entry.pack(side= tk.TOP, expand = 1)

        self.translate_button = tk.Button(
            english_tab,
            text="Translate",
            command = self.translate
            )
        self.translate_button.pack(side = tk.BOTTOM, fill= tk.X)

        self.notebook.add(english_tab, text = "English")


        spanish_tab = tk.Frame(self.notebook)
        self.notebook.add(spanish_tab, text = "Spanish")

        self.spanish_translation = tk.StringVar(spanish_tab)
        self.spanish_translation.set("No Translation")

        self.spanish_label = tk.Label(spanish_tab, textvar = self.spanish_translation)
        self.spanish_label.pack(side = tk.TOP, fill = tk.BOTH, expand=1)

if __name__ == "__main__":
    translate = Translate()
    translate.mainloop()



