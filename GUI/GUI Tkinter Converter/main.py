from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300,height=200)
window.config(pady=50,padx=50)

def cal():
    km = float(mile_input.get())*1.61
    label3.config(text=round(km,4))

label1 = Label(text="Miles",font=("Arial", 16))
label1.grid(row=1,column=5)

label2 = Label(text="is equal to",font=("Arial", 16))
label2.grid(row=2,column=1)

label3 = Label(text=0,font=("Arial", 18))
label3.grid(row=2,column=4)

label4 = Label(text="Km",font=("Arial", 16))
label4.grid(row=2,column=5)

mile_input = Entry(width=5)
mile_input.insert(END,string="0")
mile_input.grid(row=1,column=4)

button = Button(text="Calculate",command=cal)
button.grid(column=4,row=5,pady=10)





mainloop()