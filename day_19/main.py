from turtle import Turtle, Screen

t = Turtle()
screen = Screen()


def move_forward():
    t.forward(10)


def move_backwards():
    t.backward(10)


rotation_degrees = 10


def move_rotate_clockwise():
    t.setheading(t.heading() + rotation_degrees)


def move_rotate_counter():
    t.setheading(t.heading() - rotation_degrees)


def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()

# Keybinds
screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=move_rotate_counter)
screen.onkey(key="d", fun=move_rotate_clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
