import turtle
import pandas as pd
screen= turtle.Screen()
screen.title("U.S. States Game")
image = "img.gif"
screen.addshape(image)

turtle.shape(image)

data = pd.read_csv("50_states.csv")   
all_state = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_states = screen.textinput(title=f"{len(guessed_states)}/50 states", prompt= "what is the name of the state?").title()

    if answer_states == "Exit":
        missing_states = [state for state in all_state if state not in guessed_states]
        # for state in  all_state:
        #     if state not in guessed_states:
        #         missing_states.append(state) 
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break
    if answer_states in all_state:
        guessed_states.append((answer_states)) 
        tim = turtle.Turtle()
        tim.hideturtle()
        tim.penup()
        states_data = data[data.state == answer_states]
        tim.goto(int(states_data.x.item()),int(states_data.y.item()))
        tim.write(answer_states)

