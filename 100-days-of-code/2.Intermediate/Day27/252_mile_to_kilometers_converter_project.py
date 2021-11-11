from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

#Labels
is_equal_to = Label(text="is equal to", font=("Arial", 14, "bold"))
is_equal_to.grid(row=1, column=0)

miles = Label(text="Miles", font=("Arial", 14, "bold"))
miles.grid(row=0, column=2)

km = Label(text="Km", font=("Arial", 14, "bold"))
km.grid(row=1, column=2)

convert = Label(text="0", font=("Arial", 14, "bold"))
convert.grid(row=1, column=1)

#Entry
entry = Entry(width=15)
entry.grid(row=0, column=1)


#Button
def calculator():
    calc = entry.get()
    calculate = float(calc) * 1.609
    convert.config(text=f"{calculate}")


button = Button(text="Calculate", font=("Arial", 14, "bold"), command=calculator)
button.grid(row=2, column=1)


window.mainloop()
