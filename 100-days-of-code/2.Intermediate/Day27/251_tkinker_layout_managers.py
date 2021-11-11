import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=50, pady=200)

#Label
my_label = tkinter.Label(text="I am a Label", font = ("Arial", 24, "bold"))
# my_label.place(x=100, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

#change text in label
my_label["text"] = "New text"
my_label.config(text="inny")

#Button

def button_click():
    new_text = input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text="Click Me", command= button_click )
button.grid(column=1, row=1)

#New Button
new_button = tkinter.Button(text="Pause", command=button_click)
new_button.grid(column=2, row=0)

#Entry

input = tkinter.Entry(width=10)
input.grid(column=3, row=2 )


window.mainloop()
