import tkinter as ts


def change_text():
    new_text =input.get()
    my_label.config(text = new_text)

window = ts.Tk()
window.title("My first gui")
window.minsize(width = 300, height = 500)
window.config(padx=100, pady = 100)

# lable
my_label= ts.Label(text="this is lable", font = "Ariel")
# my_label.pack()
# my_label.config(text ="lable")
my_label.grid(column= 0, row= 0)
my_label.config(padx=10, pady=10)


button = ts.Button(text="click here", command = change_text)
# button.pack()
button.grid(column = 1, row = 1)

button1 = ts.Button(text = "click here again")
button1.grid(column =2 , row =0 )

input = ts.Entry(width=20)
# input.pack()
input.grid(column = 3, row= 2)


window.mainloop()