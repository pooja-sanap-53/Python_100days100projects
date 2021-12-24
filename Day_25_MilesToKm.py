# Day 25
# Date: 21 Dec 2021
# Miles to Kilometers Converter 

from tkinter import *

window = Tk()
window.title("Miles to KM Converter")
window.minsize(width=150, height=150)
window.config(padx=20, pady=20)

# Function to calculate final answer
def ans():
    ans = round(float(miles_entry.get()) * 1.60934, 2)
    km.config(text=f"{ans}")

# Labels
miles = Label(text="Miles")
miles.grid(column = 2, row=0)
km = Label(text="Km")
km.grid(column = 2, row=1)
equal = Label(text="is equal to")
equal.grid(column = 0, row=1)

km = Label(text= 0, width=15)
km.grid(column=1, row=1)

# Enteries
miles_entry = Entry(width=15)
miles_entry.grid(column=1, row=0)


# Button
cal = Button(text="Calculate", command=ans)
cal.grid(column = 1, row = 2)

window.mainloop()