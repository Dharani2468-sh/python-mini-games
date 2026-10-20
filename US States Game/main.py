import turtle

import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

#TODO: TO select the diff ty of turtle shape.
'''we can also select image as shape
    Using "addshape" to add ur image
    And then we use it at shape using .shape
'''

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image) # is actually using that default turtle and changing its shape
'''internally behaves similar to:
    default_turtle = turtle.Turtle()
    default_turtle.shape(image)
Python hides this default turtle from you.
'''
#TODO: This helps Find the location in Turtle screen
# def get_mouse_click(x, y):
#     print("Mouse click at ({},{})".format(x, y))
# turtle.onscreenclick(get_mouse_click)
# turtle.mainloop()
# '''This starts the event loop.
# Meaning:
#     “Keep checking for events continuously.”
# Like:
#     mouse click
#     keyboard press
#     screen events
# Without this, program closes immediately.
# '''

states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.values
Guessed_states = []

while len(Guessed_states) < 50:
    answer = screen.textinput(title=f"{len(Guessed_states)}/50 State Correct", prompt="What's the another state name:").title()
    if answer == "Exit":
        break
    if answer.title() in all_states:
        t = turtle.Turtle()
        state_row = states_data[states_data.state == answer.title()]
        Guessed_states.append(answer)
        t.hideturtle()
        t.penup()
        x = state_row.x.values[0]
        y = state_row["y"].values[0]
        t.goto(x, y)
        t.write(answer)

# missed_states = []
# for state in all_states:
#     if state not in Guessed_states:
#         missed_states.append(state)

#TODO: instead of having 3 to 4 lines in creating the missed_states to one line using list comprehension
missed_states =[state for state in all_states if state not in Guessed_states]
dt = pandas.DataFrame(missed_states)
dt.to_csv("missed_states.csv")

screen.exitonclick()