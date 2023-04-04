import time
import turtle
from turtle import Screen, Turtle
import pandas as pd

screen = Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
screen.tracer(0)
# def get_mouse_click_coor(x, y):
#     ''' Prints the x and y coordinates when we click on the states '''
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

i = 0
game_is_on = True
states_list = pd.read_csv("50_states.csv")
learn_states_list = states_list.state.to_list()
while game_is_on:
    screen.update()
    time.sleep(0.1)
    answer_state = screen.textinput(title=f"{i}/50 Guess the state", prompt="What's another state name").title()
    if answer_state == "Exit":
        break
    if answer_state in states_list.state.to_list():
        t = Turtle()
        t.hideturtle()
        t.penup()
        new_cor = states_list[states_list.state == answer_state]
        t.goto(new_cor.x.item(), new_cor.y.item())
        t.write(answer_state, align="center", font=("Arial", 15, "normal"))
        i += 1
        learn_states_list.remove(answer_state)

new_data = pd.DataFrame(learn_states_list)
new_data.to_csv('learn_states_list.csv')