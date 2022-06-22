from turtle import Turtle, Screen  # 常用的两个部分
import random  # 需要生成随机数字

is_race_on = False  # 用来判断比赛是否开始了
screen = Screen()  # 实例化要给屏幕
screen.setup(width=500, height=400)  # 手动对这个屏幕进行设置，使用setup函数
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")  # 让用户进行输入，涉及 screen的textinput函数
colors = ["red", "orange", "yellow", "green", "blue", "purple"]  # 生成要给颜色的列表
y_positions = [-70, -40, -10, 20, 50, 80]  # 让6个乌龟能够一字排开
all_turtles = []  # 创建一个列表来存储创建出来的乌龟

#使用for循环来创建六个乌龟
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        #230 is 250 - half the width of the turtle.
        # 先判断是否取得了胜利了
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        #接着通过随机数来让乌龟进行移动
        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()