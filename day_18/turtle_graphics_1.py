# understanding how to use turtul graphics and its documentation

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

# drawing square using turtle
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

timmy.reset()

# drawing dashed line
for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

timmy.reset()

# drawing different shapes: triangle, square ..
for angle in range(3, 11):
    for shape in range(0, angle):
        timmy.forward(100)
        timmy.right(360/angle)


screen = Screen()
screen.exitonclick()