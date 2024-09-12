"""us states game"""
import turtle
import pandas

SCREEN = turtle.Screen()
SCREEN.title("U.S. States Game")

IMAGE = "blank_states_img.gif"
SCREEN.addshape(IMAGE)

my_turtle = turtle.Turtle()
my_turtle.shape(IMAGE)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

answer_state = SCREEN.textinput(title="Guess the State", prompt="What's another state's name?")
print(answer_state)

if answer_state in all_states:
    t = turtle.Turtle()
    t.hideturtle()
    t.penup()
    state_data = data[data.state == answer_state]
    print(state_data["state"].item())
    print(state_data["x"].item())
    print(state_data["y"].item())
    t.goto(state_data.x.item(), state_data.y.item())
    t.write(state_data.state.item())

SCREEN.exitonclick()
