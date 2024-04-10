from tkinter import *

def convert_value(mile_value) -> float:
    km_value = 1.60934 * mile_value
    return km_value

def click_button():
    mile_value = entry_1.get()
    mile_value = float(mile_value)
    km_value = convert_value(mile_value)
    label_3.config(text=km_value)
       
    
converter = Tk()
converter.title("Mile to Km Converter")

converter.minsize(width=200, height=100)
converter.config(padx=30, pady=30)

label_1 = Label(text="is equal to")
label_1.grid(column=0, row=1)

label_2 = Label(text="Km")
label_2.grid(column=3, row=1)

label_3 = Label(text="0")
label_3.grid(column=2, row=1)

label_4 = Label(text="Miles")
label_4.grid(column=3, row=0)

entry_1 = Entry(width=9)
entry_1.grid(column=2, row=0, sticky="s")

button1 = Button(text="Calculate", command=click_button)
button1.grid(column=2, row=3)

converter.mainloop()
