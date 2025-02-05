# this commented code is to import and colorgram package and it allows to extract colors from any image
# import colorgram

# colors = colorgram.extract('asset/spot_painting.jpg', 30)

# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b

#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
from turtle import Turtle, Screen
import random

color_list = [(207, 160, 83), (55, 88, 131), (144, 91, 40), (139, 27, 48), (221, 207, 107), (134, 177, 202),
                (157, 47, 85), (44, 55, 105), (170, 159, 41), (129, 189, 144), (83, 20, 43), (38, 43, 66),
                (185, 94, 107), (188, 139, 166), (85, 124, 181), (60, 39, 31), (89, 157, 92), (80, 153, 164), 
                (195, 81, 72), (160, 201, 219), (45, 75, 78), (79, 75, 44), (56, 125, 121), (218, 176, 188), 
                (166, 207, 162), (220, 182, 168)]

timmy = Turtle()
timmy.speed('fastest')

screen = Screen()
screen.colormode(255)

timmy.penup()
timmy.hideturtle()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots+1):
    random_color = random.choice(color_list)
    timmy.pendown()
    timmy.dot(20, random_color)
    timmy.penup()
    timmy.forward(50)

    if dot_count % 10 == 0:
        timmy.penup()
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)



screen.exitonclick()