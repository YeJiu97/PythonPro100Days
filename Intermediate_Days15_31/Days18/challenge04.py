import turtle as t
import random

tim = t.Turtle()
tim.speed(10)
tim.pensize(10)

colours = ["Orange", "blue", "red", "green"]
directions = [0, 90, 180, 270]


for _ in range(500):
    tim.forward(30)
    tim.color(random.choice(colours))
    tim.setheading(random.choice(directions))