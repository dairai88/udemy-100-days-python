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
guessed_states = []

while len(guessed_states) < 50:
    answer_state = SCREEN.textinput(title=f"{len(guessed_states)}/50 States Correct", \
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states, columns=["State"])
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
