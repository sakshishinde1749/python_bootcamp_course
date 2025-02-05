# higher order function: giving function as a input inside any other function 
# event listeners: we can make certain events happen when user type any button on the keyboard

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def move_forward():
    timmy.forward(50)






screen.listen()
screen.onkey(key="space", fun=move_forward)

screen.exitonclick()


