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

#Buttons

def button_click():
    print("Do something")

#calls button_click() when pressed
button = tkinter.Button(text="Click Me", command= button_click )
button.pack()

#Entrries
entry = tkinter.Entry(width=30)
#add some text to begin with
entry.insert(tkinter.END, string="Some text to begin with.")
#Gets text in entry
entry.get()
entry.pack()

#Text
text = tkinter.Text(height=5, width=30)
#puts cursor in textbox
text.focus()
text.insert(tkinter.END,"Example of multi-line text entry.")
# print(text.get("1.0", tkinter.END))
text.pack()

#spinbox
def spinbox_used():
    #gets the current value in spinbox
    print(spinbox.get())

spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.pack()

#Checkbutton
def checkbutton_used():
    #prints 1 if On button checkked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checkbutton.pack()

#Radiobutton
def radio_used():
    print(radio_state.get())
#variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()

#Listbox
def lisbox_used(event):
    #gets current selections from listbox
    print(listbox.get(listbox.curselection()))
listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", lisbox_used)
listbox.pack()

window.mainloop()
