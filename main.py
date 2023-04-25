import datetime
import random
from gui import Gui
from datetime import datetime, time

AMOUNT_OF_WORDS = 5
with open(file="words.txt") as word:
    word_list = word.readlines()
    fixed = [x.replace("\n", "") for x in word_list]
    random.shuffle(fixed)
    selected_words = []
    for i in range(AMOUNT_OF_WORDS):
        selected_words.append(fixed[i])

words_as_string = ""
for word in selected_words:
    words_as_string = words_as_string + word + " "
no_space = words_as_string[0:len(words_as_string) - 1]

gui = Gui(AMOUNT_OF_WORDS)
gui.set_words(no_space)
gui.mainloop()
