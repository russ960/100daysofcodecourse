import turtle
import pandas as pd

screen = turtle.Screen()
turtle.setup(725,491)
screen.title("U.S. States Game")
image = "./25/us-states-game-start/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

state_data = pd.read_csv("./25/us-states-game-start/50_states.csv")
state_data_dict = {x[0]: x[1:] for x in state_data.itertuples(index=False)}
states_correct = []

screen_writer = turtle.Turtle()
screen_writer.penup()
screen_writer.hideturtle()
# def get_mouse_click_coor(x,y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)

while len(states_correct) < 50:
    answer_state = (screen.textinput(title=f"{len(states_correct)}/{len(state_data_dict)} States Correct", prompt="What's another state name?")).title()
    if answer_state == 'Exit':
        missing_states = state_data_dict.keys() - states_correct
        df = pd.DataFrame(missing_states, columns=["state"])
        df.to_csv('./25/missed_states.csv', index=False)
        break

    if answer_state in state_data_dict:
        states_correct.append(answer_state)
        screen_writer.goto(state_data_dict[answer_state])
        screen_writer.write(answer_state)

#screen.exitonclick()