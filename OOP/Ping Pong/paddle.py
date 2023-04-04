from turtle import Turtle

class Paddle(Turtle):

    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.speed("fast")
        self.color("white")
        self.shapesize(stretch_wid=7.0, stretch_len=1.0)
        self.penup()
        self.goto(pos)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)



