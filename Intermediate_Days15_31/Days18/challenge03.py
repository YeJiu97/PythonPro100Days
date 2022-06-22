import turtle as t
import random

tim = t.Turtle()
colours = ["red", "blue", "green", "purple"]


def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(shape_side)
