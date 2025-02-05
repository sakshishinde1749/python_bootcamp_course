# Etch-A-Sketch App

from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()

def go_forward():
    timmy.forward(50)

def go_backward():
    timmy.backward(50)

def turn_left():
    new_heading = timmy.heading() + 10
    timmy.setheading(new_heading)

def turn_right():
    new_heading = timmy.heading() - 10
    timmy.setheading(new_heading)

def clear():
    timmy.reset()


screen.listen()
screen.onkey(go_forward, "w")
screen.onkey(go_backward, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")




screen.exitonclick()
