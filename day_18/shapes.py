import random
from turtle import *

l9_turtle = Turtle()
l9_turtle.shape("turtle")
l9_turtle.color("green")
l9_turtle.speed(1)

colors = ["red", "green", "black", "yellow",
          "blue", "aquamarine", "DarkOrange",
          "DarkSeaGreen", "DeepPink", "azure4"]

def draw_shape(sides, color):
    global l9_turtle
    l9_turtle.color(color)
    angle = 360 / sides
    for _ in range(sides):
        l9_turtle.forward(100)
        l9_turtle.right(angle)

def draw():
    for sides in range(3, 11):
        draw_shape(sides, random.choice(colors))

draw()
