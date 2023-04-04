from turtle import Turtle

class Score(Turtle):
     def __init__(self):
         super().__init__()
         self.color("white")
         self.penup()
         self.hideturtle()
         self.l_score = 0
         self.r_score = 0
         self.update()
     def update(self):
         self.clear()
         self.goto(0,300)
         self.write("│--│", align="center", font=("Courier", 80, "normal"))
         self.goto(-100, 300)
         self.write(f"{self.l_score}", align="center", font=("Courier", 80, "normal"))
         self.goto(100, 300)
         self.write(self.r_score, align="center", font=("Courier", 80, "normal"))
     def l_point(self):
         self.l_score += 1
         self.update()
     def r_point(self):
         self.r_score += 1
         self.update()