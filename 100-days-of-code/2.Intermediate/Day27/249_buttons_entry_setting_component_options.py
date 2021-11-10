import tkinter

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

#Label
my_label = tkinter.Label(text="I am a Label", font = ("Arial", 24, "bold"))
my_label.pack()

#change text in label
my_label["text"] = "New text"
my_label.config(text="inny")

#Button

def button_click():
    new_text = input.get()
    my_label.config(text = new_text)

button = tkinter.Button(text="Click Me", command= button_click )
button.pack()

#Entry

input = tkinter.Entry(width=10)
input.pack()


window.mainloop()
