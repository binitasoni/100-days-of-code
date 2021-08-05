from tkinter import *
def button_clicked():
    a=mile_input.get()
    b=float(a)*1.609
    ans_label.config(text=b)




mile_input=Entry(width=10)
mile_input.grid(column=1,row=0)

miles_label=Label(text="Miles",font=("Arial","24"))
miles_label.grid(column=2,row=0)

is_label=Label(text="is equal to",font=("Arial","24"))
is_label.grid(column=0,row=1)

ans_label=Label(text=" ",font=("Arial","24"))
ans_label.grid(column=1,row=1)

km_label=Label(text="km",font=("Arial","24"))
km_label.grid(column=2,row=1)

button2=Button(text="Calculate", command=button_clicked)
button2.grid(column=1,row=2)
mainloop()