from turtle import Turtle, Screen

'''to do 

w = forwards
s = backwards
a = conter-clockwise
d = clockwise
c = clear drawn

'''

# 首先是一个Turtle的对象
tim = Turtle()
screen = Screen()

# 移动函数
def move_forwards():
	tim.forward(20)

def move_backwards():
	tim.backward(20)

def turn_left():
	new_heading = tim.heading() + 10  # 角度每次 +10
	tim.setheading(new_heading)  # 将new_heading设置为heading

def turn_right():
	new_heading = tim.heading() -10  # 角度每次 +10
	tim.setheading(new_heading)  # 将new_heading设置为heading

def clear():
	tim.clear()  # 将海龟的图像清除掉
	tim.penup()  # 这样一来turtle回归的时候就不会画出横线了，因为pen已经up了
	tim.home()  # 将海龟的图标回归原点

# 开始实现功能
screen.listen()

# 开始进行移动
screen.onkey(move_forwards, "w")
screen.onkey(move_backwards, "s")
screen.onkey(turn_left, "a")
screen.onkey(turn_right, "d")
screen.onkey(clear, "c")

# 让屏幕保持住
screen.exitonclick()