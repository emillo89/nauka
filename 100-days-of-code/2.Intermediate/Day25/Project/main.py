import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)



states_data = pandas.read_csv("50_states.csv")
all_states = states_data.state.to_list()

def create_turtle(answer_state, data):
    text = turtle.Turtle()
    text.hideturtle()
    text.penup()
    row = data[data.state == answer_state]
    print(row.x)
    text.goto(x= int(row.x), y=int(row.y))
    text.write(row.state.item(), font=('Arial', 8, "normal"))

#if states_data is one of the states in all the states of the 50_states.csv
    # if they got it right
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state in all_states :
        # Create a turtle to write the name of the state at the state's x and y coordate
        create_turtle(answer_state,states_data)
        guessed_states.append(answer_state)
    elif answer_state == "Exit":
        #Use a list comprehension
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break




# def get_mouse_click_coor(x, y):
#     print(x,y)
#
# turtle.onscreenclick(get_mouse_click_coor)
#
# turtle.mainloop()

