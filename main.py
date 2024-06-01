from turtle import Turtle, Screen
import random




#setup generate 8 turtles

colors = ["red", "blue", "green", "yellow", "black", "orange", "purple", "brown"]
screen = Screen()
choice = screen.textinput("who will win", "color of turtle")
def create_turtle(color,x,y):
    t = Turtle()
    t.shape('turtle')
    t.penup()
    t.goto(x,y)
    t.color(color)
    return t

x_lane = -400
y_lane = -200

turtles = []
for color in colors:
    turtles.append(create_turtle(color,x_lane,y_lane))
    y_lane+=50
    
#setup 8 lanes


game_going = True
while game_going:
    for turtle in turtles:
        x = random.randint(10,30)
        turtle.forward(x)
        pos = turtle.pos()
        if int(pos[0]) > 400:
             
            if choice == turtle.color()[0]:
                print("you chose the right one, you win")
            else:
                print("lost, you chose the wrong turtle")
            game_going = False
            break
        print(f"{pos[0],turtle.color}")



screen.exitonclick()