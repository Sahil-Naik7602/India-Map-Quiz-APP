import turtle
import pandas as pd

screen = turtle.Screen()
screen.setup(height=800,width=600)
image = "political-map.gif"
screen.addshape(image)
turtle.shape(image)
is_game_on = True
guess_state = []

data = pd.read_csv("india-states.csv")
all_states = data.subdivision_name.to_list()

while len(guess_state)<29:
    my_input = screen.textinput(title=f"{len(guess_state)}/29 guessed",prompt="Write the name of the state: ").title()
    if my_input in all_states:
        guess_state.append(my_input)
        data.reset_index(drop=True,inplace=True)
        x_cor = data[data.subdivision_name==my_input].x_axis
        y_cor = data[data.subdivision_name==my_input].y_axis
        text=turtle.Turtle()
        text.ht()
        text.penup()
        text.goto(int(x_cor),int(y_cor))
        text.write(f"{my_input}",False, align = "center", font = ("Arial",10,"bold"))

    if my_input=="Quit":
        #states not guessed to be stored in a csv file
        states_to_learn = all_states
        for names in guess_state:
            if names in states_to_learn:
                states_to_learn.remove(names)

        if states_to_learn==[]:
            print("Good You know all state's name")
        elif states_to_learn!=[]:
            pd.DataFrame(states_to_learn).to_csv("states_to_learn")
        break


screen.exitonclick()