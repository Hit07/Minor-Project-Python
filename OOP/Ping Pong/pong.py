from turtle import Turtle
import random as r
class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.shapesize(stretch_wid=0.50, stretch_len=0.50)
        self.penup()
        self.x_cor = 10
        self.y_cor = 10
        self.move_speed = 0.1
    def loc(self):
        x = self.xcor() + self.x_cor
        y = self.ycor() + self.y_cor
        self.goto(x, y)
        # self.speed("slowest")
    def bounce(self):
        self.y_cor *= -1
    def hit(self):
        self.x_cor *= -1
        self.move_speed *= 0.9
    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.hit()

