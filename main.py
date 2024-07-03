from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = ()

try:
    data = pd.read_csv("words_to_learn.csv.csv", usecols=["hindi", "english"])
except FileNotFoundError:
    original_data = pd.read_csv("Untitled spreadsheet - Sheet1.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    # print(to_learn)


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # print(current_card['hindi'])
    canvas.itemconfig(card_title, text="Hindi", fill="black")
    canvas.itemconfig(card_word, text=current_card['hindi'], fill="black")
    canvas.itemconfig(card_background, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card['english'], fill="white")
    canvas.itemconfig(card_background, image=card_back)


def is_know():
    to_learn.remove(current_card)
    print(len(to_learn))
    new_data = pd.DataFrame(to_learn)
    new_data.to_csv("words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Put image into code

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file="D:/PycharmProjects/Flase_card/images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 264, image=card_front)
card_title = canvas.create_text(400, 150, text="", fill="black", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", fill="black", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

# put button image into file

my_wrong = PhotoImage(file="D:/PycharmProjects/Flase_card/images/wrong.png")
wrong_button = Button(image=my_wrong, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)
# wrong_button.config

my_right = PhotoImage(file="D:/PycharmProjects/Flase_card/images/right.png")
right_button = Button(image=my_right, highlightthickness=0, command=is_know)
right_button.grid(column=1, row=1)

next_card()

# read csv file


window.mainloop()
