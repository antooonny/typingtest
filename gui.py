import tkinter
from tkinter import END
from datetime import datetime
import random

class Gui(tkinter.Tk):
    def __init__(self, amount):
        super().__init__()
        self.amount_of_words = amount
        self.canvas = tkinter.Canvas(width=400, height=400)
        self.canvas.grid(row=0, column=0)
        self.label = tkinter.Label(text="test", font=("Ariel", 24, "bold"), wraplength=300)
        self.wpm = tkinter.Label(text="", font=("Ariel", 24, "bold"), wraplength=300)
        self.wpm.grid(row = 1, column=0)
        self.var_entry = tkinter.StringVar()
        self.entry = tkinter.Entry(width=50, textvariable=self.var_entry)
        self.entry.grid(row=2, column=0, columnspan=2)
        self.label.grid(column=0, row=0)
        self.button = tkinter.Button(text="Reset", command=self.reset)
        self.button.grid(row=2,column=1)
        self.word_list = ""
        self.var_entry.trace_add("write", callback=self.change_word)
        self.word_number = 0
        self.start_time = ""
        self.end_time = ""
        self.one_time = True
        self.time = 0


    def new_words(self):
        with open(file="words.txt") as word:
            word_list = word.readlines()
            fixed = [x.replace("\n", "") for x in word_list]
            random.shuffle(fixed)
            selected_words = []
            for i in range(self.amount_of_words):
                selected_words.append(fixed[i])

        words_as_string = ""
        for word in selected_words:
            words_as_string = words_as_string + word + " "

        no_space = words_as_string[0:len(words_as_string) - 1]
        self.set_words(no_space)

    def set_words(self, word_list):

        self.label.config(text=word_list)
        self.word_list = word_list

    def calculate_wpm(self):
        time_total = self.end_time - self.start_time
        time_in_seconds = time_total.total_seconds()
        time_in_minutes = time_in_seconds / 60
        self.time = round(self.amount_of_words / time_in_minutes)

    def display_score(self):
        self.entry.delete(0, END)
        self.calculate_wpm()
        self.wpm.config(text=f"WPM: {self.time}")

    def change_word(self, *args):
        if self.entry.get() != "" and self.one_time:
            self.start_time = datetime.now()
            self.one_time = False

        if self.entry.get() == self.word_list[0:len(self.entry.get())]:
            self.label.config(fg="green")
            if self.entry.get() == self.word_list:
                self.end_time = datetime.now()
                self.display_score()

        else:
            self.label.config(fg="red")


    def reset(self):
        self.entry.delete(0, END)
        self.label.config(fg="black")
        self.new_words()
        self.start_time = datetime.now()
        self.wpm.config(text="")







