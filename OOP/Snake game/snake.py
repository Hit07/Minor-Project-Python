from turtle import Turtle
POSITIONS = [(0,00), (-20,0), (-40,0)]
SPEED = "normal"
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for i in POSITIONS:
            self.add_square(i)
    def add_square(self, i):
        square = Turtle("square")
        square.speed(SPEED)
        square.color("white")
        square.penup()
        square.goto(i)
        self.segments.append(square)
    def grow(self):
        # print(self.segments[-1].position())
        self.add_square(self.segments[-1].position())
    def move(self):
        for seg in range(len(self.segments)-1, 0 , -1):
            new_x = self.segments[seg-1].xcor()
            new_y = self.segments[seg-1].ycor()
            self.segments[seg].goto(new_x,new_y)
        self.head.forward(MOVE)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(10000,10000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        # self.head.goto(0,0)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)