from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"

current_cards = {}
to_learn ={}

try:
    data = pd.read_csv("data/to_learn.csv")
except:
    original_data = pd.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient= "records")
else:
    to_learn= data.to_dict(orient= "records")


def next_cards():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card= random.choice(to_learn)
    canva.itemconfig(card_title, text= "French", fill= "black")
    canva.itemconfig(card_word, text = current_card["French"], fill="black")
    canva.itemconfig(card_background, image = card_front)
    flip_timer = window.after(3000, func= flip_card)

def flip_card():
    canva.itemconfig(card_title, text = "English", fill = "white")
    canva.itemconfig(card_word, text = current_card["English"], fill ="white")
    canva.itemconfig(card_background, image = card_back )

def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/to_learn.csv",index = False)

    next_cards()


window = Tk()
window.title("Flash card")
window.config(padx = 50, pady= 60, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, func= flip_card)

canva = Canvas(width = 800, height = 526)
card_front = PhotoImage(file = "images/card_front.png")
card_back= PhotoImage(file= "images/card_back.png")
card_background= canva.create_image(400,263,image =card_front)
card_title =canva.create_text(400,150,text =  "title", font = ("Ariel",40,"italic"))
card_word = canva.create_text(400,260,text =  "title", font = ("Ariel",60,"bold")) 
canva.config(bg = BACKGROUND_COLOR ,highlightthickness= 0)
canva.grid(column = 0, row = 0, columnspan= 3 )

wrong_image= PhotoImage(file = "images/wrong.png")
wrong= Button(image = wrong_image,highlightthickness=0, command=next_cards)
wrong.grid(column =0 , row = 1)

right_image = PhotoImage(file = "images/right.png")
right = Button(image= right_image,bg = BACKGROUND_COLOR, command= is_known)
right.grid(column = 2 , row = 1)

next_cards()
window.mainloop()