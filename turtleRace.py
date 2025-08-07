from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500 , height=400)
user = screen.textinput(title="Please select your choice's", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "black","green", "blue", "purple"]
y_position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_position[turtle_index])
    all_turtle.append(new_turtle)


if user:
    is_race_on = True

while is_race_on:

    for turtle in all_turtle:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost!! The {winning_color} turtle is the winner!")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()