from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
     global reps 
     reps += 1

     work_sec= WORK_MIN *60
     short_break= SHORT_BREAK_MIN * 60
     long_break= LONG_BREAK_MIN *60
 
     if reps % 8 == 0:
         count_down(long_break)
         timer.config(text= "BREAK " ,fg= RED)
     elif reps % 2== 0 :
          count_down(short_break)
          timer.config(text="Break", fg = PINK)
     else:
          count_down(work_sec)
          timer.config(text = " WORK " , fg = GREEN)

     # count_down(    )

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count% 60
    if count_sec ==0:
         count_sec= "00"
    canva.itemconfig(timer_text , text= f"{count_min}:{count_sec}")
    if count> 0 :
         window.after(1000,count_down, count-1)
    else:
         start_timer()
         mark= ""
         work_sessions = math.floor(reps/2)
         for _ in range (work_sessions):
              mark+= "✅"
# ---------------------------- UI SETUP ------------------------------- #
window= Tk()
window.title("Pomodoro ")
window.config(padx=100, pady=50, bg = YELLOW)

# timer font
timer=Label(text = "Timer" ,font = ("Courier", 35, "bold"), fg = GREEN, bg = YELLOW)
timer.grid(column= 1, row =0)

# image
canva= Canvas(width=220, height=225,bg = YELLOW,highlightthickness=0 )
tomato = PhotoImage(file= "tomato.png")
canva.create_image(104,112, image= tomato)
timer_text = canva.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME, 25 ,"bold"))
canva.grid(column = 1, row =1)


# start button
start = Button(text = "START", highlightthickness=0, command = start_timer)
start.grid(column= 0, row =2)

# reset button
reset= Button(text= "RESET", highlightthickness =0)
reset.grid(column = 2, row =2)

# check marks

check =Label(text = "✓" , fg= GREEN , bg = YELLOW)
check.grid(column=1, row=4)


window.mainloop()