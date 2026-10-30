from tkinter import *
from tkinter import messagebox
from random import  choice , randint, shuffle
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password(): 
    letter= ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    number =['1','2','3','4','5','6','7','8','9','0']
    symbol=['!','@','#','$','%','^','&','*','(',')']

    password_letter=[choice(letter) for _ in range(randint(8,10))]
    password_number=[choice(number) for _ in range(randint(2,4))]
    password_symbol=[choice(symbol) for _ in range(randint(2,4))]
    password_list = password_letter + password_number + password_symbol
    shuffle(password_list)

    passwords = "".join(password_list) 
    pass_entry.insert(0,passwords)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    web = web_entry.get()
    emaill= email_entry.get()
    pas = pass_entry.get()
    new_data = {
         web: {
             "email" : emaill,
             "password" : pas
         }
    }
    if len(web) == 0 or len(pas) == 0:
            messagebox.showwarning(title = "Warning",message= "Don't leave field empty")
    else: 
        try:
            with open("data.json","r" ) as data_file:
                #  read old data
                data= json.load(data_file)
        except:
            with open("data.json", "w ") as data_file:
                json.dump(new_data, data_file, indent = 4)
        else:    
            # update old data with new data 
            data.update(new_data)
        
            with open("data.json","w") as data_file:     
                json.dump(data , data_file, indent = 4)
        finally :
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

# ---------------------- FIND PASSWORD -------------------------------- #
def find_password():
    web = web_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except:
        messagebox.showinfo(title = "Error", message = "No data file found ")
    else:
        if web in data:
            email = data[web]["email"]
            password = data[web]["password"]
            messagebox.showinfo(title= website , message = f"email:{email}\n password : {password}")
        else: 
            messagebox.showinfo(title= "Error", message= f"No detail for {web} found")
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady = 50)

lock= PhotoImage(file = "logo.png")
canva = Canvas(width = 200, height = 200)
canva.create_image(100,100,image =lock)
canva.grid(column=1, row = 0)

website = Label(text = "Website:")
website.grid(column=0 , row = 1)
email=   Label(text= "Email/Username:")
email.grid(column= 0, row = 2)
password=Label(text= "Password:" )
password.grid(column= 0, row =3)

web_entry = Entry(width = 21)
web_entry.grid(column= 1 , row = 1)
web_entry .focus()
email_entry= Entry(width = 39)
email_entry.grid(column= 1, row = 2, columnspan=3)
email_entry.insert(0,"krishnanandy379@gmail.com")
pass_entry= Entry(width =21)
pass_entry.grid(column= 1, row = 3)

search = Button(text= "Search", command = find_password)
search.grid(column = 2 , row = 1)
generate= Button(text = "generate password", command= generate_password)
generate.grid(column = 2,row = 3)

add= Button(text = "Add Password", width =36, command= save )
add.grid(column=0, row = 4, columnspan=3)
window.mainloop()