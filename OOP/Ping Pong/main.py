from turtle import Turtle,Screen
from paddle import Paddle
from pong import Pong
from score import Score
import time

screen = Screen()
screen.setup(width=1000,height=1000)
screen.bgcolor("black")
screen.title("Pong")

screen.tracer(0)
paddle_l = Paddle((-450,0))
paddle_r = Paddle((450,0))
pong = Pong()
score = Score()

screen.listen()
screen.onkey(paddle_l.up ,"Up")
screen.onkey(paddle_l.down ,"Down")
screen.onkey(paddle_r.up ,"q")
screen.onkey(paddle_r.down ,"a")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(pong.move_speed)
    pong.loc()
    '''Detecting collision by wall'''
    if pong.ycor() > 380 or pong.ycor() < -380:
        pong.bounce()
    '''Detecting collision with paddle'''
    if pong.distance(paddle_r) <= 50 and pong.xcor() > 360 or pong.distance(paddle_l) <= 50 and pong.xcor() < -360:
        pong.hit()
    '''Detecting collision with wall for point'''
    if 480 < pong.xcor():
        pong.reset_position()
        score.l_point()
    if pong.xcor() < -480:
        pong.reset_position()
        score.r_point()








screen.exitonclick()