import tkinter as ts

window= ts.Tk()
window.title("milesconverter")
window.minsize(width = 300, height = 50)
window.config(padx=20, pady = 20)

def calculate():
    miles = float(entry.get())
    km = miles*1.609
    result.config(text=f"{km}" )

entry = ts.Entry()
entry.grid(column=1 ,row=0)

miles=ts.Label(text="enter miles")
miles.grid(column=2, row =0)

is_equal= ts.Label(text="is equal to")
is_equal.grid(column=0 , row =1)

result=ts.Label(text = "0")
result.grid(column=1, row =1)

kilometers=ts.Label(text = "kilometers")
kilometers.grid(column = 2, row = 1)

calculate= ts.Button(text ="calculate", command= calculate)
calculate.grid(column=1, row= 2)

window.mainloop()