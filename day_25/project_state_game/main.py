import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S.A state game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

timmy = turtle.Turtle()

guessed_state = []

data = pandas.read_csv("50_states.csv")
all_states = data.state.tolist()

while len(guessed_state) <= 50:

    answer_state = screen.textinput(title=f"{guessed_state}/50 Guess the state", prompt="What is the another state name?").title()

    if answer_state == "Exit":
        missing_state = [state for state in all_states if state not in guessed_state]
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
    


