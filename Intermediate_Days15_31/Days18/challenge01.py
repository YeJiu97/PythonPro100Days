import turtle as t

# from turtle import Turtle
# 这样就不需要一直写turtle.Turtle
# 不建议使用 from turtle import *，虽然这样允许直接使用函数，但是会导致阅读障碍

timmy_the_turtle = t.Turtle()  # 使用Turtle()来实例化一个对象
timmy_the_turtle.shape("turtle")  # 将shape设定为turtle
timmy_the_turtle.color("blue")  # 将颜色设置为红色

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.left(90)

# 让界面停留
screen = t.Screen()
screen.exitonclick()
