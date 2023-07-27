import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_state = []

score = 0
for i in range(50):
    answer_state = screen.textinput(title=f"{score}/50 states correct", prompt="What's the another state name? ").title()

    if answer_state == "Exit":
        #Using list comprehension
        missing_states = [state for state in states if state not in guessed_state]
        # missing_states = []
        # for state in states:
        #     if state not in guessed_state:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in states:
        guessed_state.append(answer_state)
        score += 1
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())    #or t.write(answer_state)

