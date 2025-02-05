from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter color: ")

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_names = ["tom", "timmy", "jim", "nany", "oreo", "jerry"]
x_cordinate = -230
y_cordinate = -100

for turtle_index in range(6):

    turtle_names[turtle_index] = Turtle(shape="turtle")
    turtle_names[turtle_index].color(colors[turtle_index])
    turtle_names[turtle_index].penup()
    turtle_names[turtle_index].goto(x=x_cordinate, y=y_cordinate)

    y_cordinate += 40

if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in turtle_names:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()

            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner")
            else:
                print(f"You have lost. The {winning_color} turtle is the winner")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    












screen.exitonclick()
