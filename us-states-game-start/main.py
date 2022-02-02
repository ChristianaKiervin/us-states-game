import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")

# load the image as the screen shape

image = "blank_states_img.gif"  # store image path
screen.addshape(image)
turtle.shape(image)

# setup variables and data

correctGuessList = []
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()

# create game

while len(correctGuessList) < 50:
    # calls a pop-up text box and converts answers to title case
    guess = screen.textinput(title=f"{len(correctGuessList)}/50 States Correct",
                             prompt="What's another state's name?").title()

    #Generate list of states not learned by user upon exit
    if guess == "Exit":
        missedStates = [state for state in states if state not in correctGuessList]
        newData = pandas.DataFrame(missedStates)
        newData.to_csv("states_to_learn.csv")
        break

    # Update guess list and map with state name if correct
    if guess in states:
        correctGuessList.append(guess)  # add guess to list
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        stateData = data[data.state == guess]
        t.goto(int(stateData.x), int(stateData.y))
        t.write(guess)