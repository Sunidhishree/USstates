from turtle import Turtle,Screen
import pandas
t=Turtle()
screen=Screen()
screen.title("US States Game")
img="blank_states_img.gif"
screen.addshape(img)
t.shape(img)
l=0
guess=[]
game=True
while game:
        answer= screen.textinput(title=f"Guess state [{l}/50]",prompt="Enter name")

        data= pandas.read_csv("50_states.csv")
        state= data.state.to_list()

        if answer.title() in state:
                l+=1
                turtle=Turtle()
                turtle.hideturtle()
                turtle.penup()
                sta=data[data.state == answer.title()]
                turtle.goto(sta.x.item(),sta.y.item())
                turtle.pendown()
                turtle.write(answer.title())
                guess.append(answer.title())
        if answer.lower()=='quit':
                missing=[]
                for i in state:
                        if i not in guess:
                                missing.append(i)
                print(missing)
                game=False

screen.exitonclick()


