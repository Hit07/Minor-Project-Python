from turtle import Turtle,Screen
import random as r

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.shapesize(stretch_wid=0.50,stretch_len=0.50)
        self.speed("fastest")
        self.loc()

    def loc(self):
        x = r.randint(-280,280)
        y = r.randint(-280,280)
        self.goto(x,y)




