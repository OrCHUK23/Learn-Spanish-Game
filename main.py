from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

to_learn = {}
# Read the spanish_words csv file to list of dictionaries
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError as e:
    print("Could'nt find words to learn, fetching original words file.")
    original_data = pandas.read_csv("./data/spanish_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
current_card = {}


def next_card():
    """
    Function handles next card after button has been clicked by the user.
    """
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Spanish", fill="black")
    canvas.itemconfig(card_word, text=current_card["Spanish"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    """
    Function removes the current card from the cards that are in the list of words to learn.
    """
    to_learn.remove(current_card)
    to_learn_data = pandas.DataFrame(to_learn)
    to_learn_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)

def countdown(count):
    """
    Function handles countdown of the cards.
    :param count: number of second for each card before it flips.
    """
    window.after(1000, countdown, count - 1)


# ----------- WINDOW SETUP ----------- #
window = Tk()
window.title("Flash Cards - Spanish To English")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# ----------- COUNTDOWN MECHANISM ----------- #
flip_timer = window.after(3000, func=flip_card)

# ----------- UI SETUP  ----------- #
# Front card setup.
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = canvas.create_image(400, 263, image=card_front_img)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 300, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Known answer setup.
right_pic = PhotoImage(file="./images/right.png")
known_button = Button(image=right_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=is_known)
known_button.grid(row=1, column=1)

# Unknown answer setup.
wrong_pic = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=wrong_pic, highlightthickness=0, bg=BACKGROUND_COLOR, command=next_card)
unknown_button.grid(row=1, column=0)

next_card()
window.mainloop()
