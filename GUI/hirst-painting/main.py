import turtle

import colorgram
import random
from turtle import Turtle,Screen
tim = Turtle()
turtle.colormode(255)
# Extract 6 colors from an image.
# rgb_color = []
# colors = colorgram.extract('image.jpg', 20)
# print(colors)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_color.append((r, g, b))
# print(rgb_color)
color_list = [(237, 34, 109), (153, 24, 65), (240, 73, 34), (7, 147, 92), (218, 170, 46), (179, 158, 44),
              (25, 123, 190), (44, 190, 232), (83, 20, 77), (244, 220, 47), (252, 223, 1), (125, 192, 84),
              (183, 39, 104), (207, 63, 24), (56, 172, 103), (170, 24, 19)]

tim.penup()
tim.setposition(-200.00,-200)
tim.penup()
tim.speed("fastest")
def func1():
    for i in range(10):
        tim.dot(20,random.choice(color_list))
        tim.penup()
        tim.forward(50)
    func2()
def func2():
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.seth(0)

for i in range(10):
    func1()
tim.hideturtle()

screen = Screen()
screen.exitonclick()
