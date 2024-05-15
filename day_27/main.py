from tkinter import *

win = Tk()
win.title("Temperature Converter")
win.minsize(width=200, height=100)
win.config(padx=20, pady=20)

# text input
input = Entry(width=7)
input.insert(END, 0)
input.grid(column=1, row=0)

# labels
Label(text="Fahrenheit").grid(column=2, row=0)
Label(text="is equal to").grid(column=0, row=1)
result = Label()
result.grid(column=1, row=1)
Label(text="Celsius").grid(column=2, row=1)


# button
def calculate():
    calculation = round((int(input.get()) - 32) * (5 / 9), 1)
    result.config(text=calculation)


Button(text="Calculate", command=calculate).grid(column=1, row=2)

win.mainloop()
