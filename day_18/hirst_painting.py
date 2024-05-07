import turtle as t
import random

t.colormode(255)
turtle = t.Turtle()
turtle.speed("fastest")
turtle.hideturtle()

colors = [(245, 241, 233), (227, 234, 242), (245, 234, 239),
          (233, 242, 236), (208, 158, 96), (234, 213, 101),
          (41, 104, 144), (149, 78, 57), (130, 168, 194), (202, 137, 162)]

turtle.penup()
turtle.setheading(225)
turtle.forward(300)
turtle.setheading(0)

for _ in range(10):
    for _ in range(10):
        turtle.dot(20, random.choice(colors))
        turtle.forward(50)
    turtle.setheading(90)
    turtle.forward(50)
    turtle.setheading(180)
    turtle.forward(500)
    turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()
