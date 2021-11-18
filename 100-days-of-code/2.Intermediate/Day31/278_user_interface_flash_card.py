from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

canvas_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
img_front = PhotoImage(file="images/card_front.png")
canvas_front.create_image(410, 263, image=img_front)
canvas_front.grid(column=0, row=0, columnspan=2)
canvas_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
canvas_front.create_text(400, 263, text="word", font=("Ariel", 40, "bold"))

cross_image = PhotoImage(file="images/wrong.png")
cancel_button = Button(image=cross_image, highlightthickness=0)
cancel_button.grid(column=0, row=1)

check_image = PhotoImage(file="images/right.png")
check_button = Button(image=check_image, highlightthickness=0)
check_button.grid(column=1, row=1)
window.mainloop()
