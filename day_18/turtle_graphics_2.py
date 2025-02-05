from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.pensize(15)
timmy.speed("fastest")

screen = Screen()
screen.colormode(255)

directions = [0, 90, 180, 270]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# draw random walk
for _ in range(200):
    direction = random.choice(directions)
    timmy.color(random_color())

    timmy.forward(30)
    timmy.setheading(direction)




screen.exitonclick()


