from turtle import Turtle,Screen
screen = Screen()
ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270.00)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"  Score: {self.score}   |   High Score: {self.high_score} ", align=ALIGNMENT, font=FONT)
        # self.data.close()

    def reset_high_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()


    # def game_over(self):
    '''Displays Game over message whenever snake hits the wall or itself'''
    #     self.goto(0,0)
    #     self.write(f"Game Over !!😵‍💫", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()