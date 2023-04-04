from turtle import Screen
from snake import Snake
from Food import Food
from score import Score
import time


screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Game Score")

screen.tracer(0)
snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up ,"Up")
screen.onkey(snake.down ,"Down")
screen.onkey(snake.left ,"Left")
screen.onkey(snake.right ,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    '''Detecting collision with food'''
    if snake.head.distance(food) <= 15:
        food.loc()
        snake.grow()
        score.increase_score()
    '''Detecting collision with wall'''
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        score.reset_high_score()
        snake.reset_snake()
    '''Detecting collision with itself'''
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            score.reset_high_score()
            snake.reset_snake()

screen.exitonclick()


# class Animal:
#     def __init__(self):
#         self.eyes = 2
#     def breathe(self):
#         print("Inhale\nExhale")
# class Fish(Animal):
#     def __init__(self):
#         super().__init__()
#     def breathe(self):
#         super().breathe()
#         print("through gills")
#     def swim(self):
#         print("Swimming in water")
#
# nemo = ()
# nemo.breathe()
