from tkinter import *
import pandas
import random

data = pandas.read_csv("../Day31/words_to_learn.csv")
to_learn = data.to_dict(orient="records")
current_card= {}
print(to_learn)

def random_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    word = current_card['French']
    canvas_front.itemconfig(card_title, text="French", fill="black")
    canvas_front.itemconfig(card_word, text=word, fill="black")
    flip_timer = window.after(3000,func = flip_card)

def flip_card():
    word_english = current_card["English"]
    canvas_front.itemconfig(card_title,text="English", fill="white")
    canvas_front.itemconfig(card_word,text=word_english, fill="white")
    canvas_front.itemconfig(front_card, img=img_back)

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="../Day31/images/card_front.png")
img_back = PhotoImage(file="../Day31/images/card_back.png")
front_card = canvas_front.create_image(410, 263, image=img_front)
canvas_front.grid(column=0, row=0, columnspan=2)
card_title = canvas_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas_front.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

cross_image = PhotoImage(file="../Day31/images/wrong.png")
cancel_button = Button(image=cross_image, highlightthickness=0, command = random_word)
cancel_button.grid(column=0, row=1)

check_image = PhotoImage(file="../Day31/images/right.png")
check_button = Button(image=check_image, highlightthickness=0, command = random_word)
check_button.grid(column=1, row=1)
window.mainloop()