from tkinter import *
window = Tk()
window.title("Miles to KM")
window.minsize(width=500, height=500)
window.config(padx=50, pady=50)

def calculate():
    # print("calculate")
    mile = float(entry.get())
    kmn = mile*1.609
    kmm = round(kmn,2)
    kms.config(text=f"{kmm}")
#create lables 4
is_equal_to = Label()
is_equal_to.config(text="is Equal to:")
is_equal_to.grid(column=0, row=1)

miles = Label()
miles.config(text="Miles")
miles.grid(column=2, row=0)

km = Label()
km.config(text="Km")
km.grid(column=2, row=1)

kms = Label()
kms.config(text="0")
kms.grid(column=1, row=1)

#entry
entry = Entry(width=10)
entry.insert(END,string="0")
entry.grid(column=1,row=0)
entry.focus

#button
button = Button(text="Calculate",command=calculate)
button.grid(column=1,row=2)












window.mainloop()