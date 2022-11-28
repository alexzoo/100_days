import turtle
import pandas

screen = turtle.Screen()
screen.title('US States Game')
image = 'day25/blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv('day25/50_states.csv')
all_states = data['state'].to_list()
guessed_state = []

while len(guessed_state) < 50:

    answer_state = screen.textinput(
        f'{len(guessed_state)}/50 States Correct', prompt='What\'s another state\'s name?').title()
    if answer_state == 'Exit':
        missing_states = []
        for state in all_states:
            if state not in guessed_state:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv('day25/states_to_learn.csv')
        break

    if answer_state in all_states:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
