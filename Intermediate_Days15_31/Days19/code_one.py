# 函数：listen()，这个是turtle提供的函数，可以用来监听并且等待
from turtle import Turtle, Screen


tim = Turtle()
screen = Screen()

def move_forwards():
	tim.forward(10)

screen.listen()
# key = "space" 意味着只有在空格键被按下去的时候才会运行
# fun是screen内置的函数，所以fun=move_forwards相当于将函数作为参数传入另一个函数
# 在函数作为参数的时候，不需要加上()
screen.onkey(key="space", fun=move_forwards)  

# 让screen在运行的时候不会退出
screen.exitonclick()