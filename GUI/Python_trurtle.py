import turtle
from turtle import Turtle,Screen
import random as r


tim = Turtle()
screen = Screen()
tim.shape("turtle")
tim.color("black","green")
turtle.colormode(255)
def random_color():
    r1 = r.randint(0,255)
    g = r.randint(0,255)
    b = r.randint(0,255)
    return (r1,g,b)
    # return(r,g,b)

# while True:
#     tim.forward(100)
#     tim.left(90)
# for i in range(20):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# while True:
#     count += 1
#     if count < 4:
#         tim.forward(100)
#         tim.left(120)
#     elif count < 9 and count > 4:
#         tim.pencolor("red")
#         tim.forward(100)
#         tim.left(90)
#     elif count < 15 and count > 9:
#         tim.pencolor("blue")
#         tim.forward(100)
#         tim.left(72)
#     elif count < 22 and count > 15:
#         tim.pencolor("green")
#         tim.forward(100)
#         tim.left(60)
#     elif count < 30 and count > 22:
#         tim.pencolor("orange")
#         tim.forward(100)
#         tim.left(51.42)
#     elif count < 39 and count > 30:
#         tim.pencolor("brown")
#         tim.forward(100)
#         tim.left(45)
#     elif count < 49 and count > 39:
#         tim.pencolor("pink")
#         tim.forward(100)
#         tim.left(40)
#     elif count < 60 and count > 49:
#         tim.pencolor("black")
#         tim.forward(100)
#         tim.left(36)
# """Method: 2"""
# number_sides = 10
# # color = ["red","blue","purple","black","orange","violet","dark green","pink","silver"]
# color = random_color()
# while number_sides:
#     # tim.pencolor(color)
#     angle = 360 / number_sides
#     for _ in range(number_sides):
#         tim.pencolor(color)
#         tim.forward(100)
#         tim.left(angle)
#     number_sides -= 1
# def direction(angle,color):
#         tim.seth(angle)
#         tim.pencolor(color)
#         tim.pensize(18)
#         tim.forward(15)
#
# tim.pencolor("white")
# tim.setx(-100.00)
# for i in range(200):
#     tim.speed("fastest")
#     color = random_color()
#     angle = r.choice([0,90,180,270,360])
#     direction(angle,color)
# for i in range(150):
#     tim.color(random_color())
#     tim.speed("fastest")
#     tim.ht()
#     tim.circle(100)
#     tim.right(-3.50)
# =============================================================================================#

screen.exitonclick()