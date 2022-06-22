from turtle import Screen  # 导入Turtle的screen
from snake import Snake  # 从snake类种导入Snake函数
import time  # 导入时间模块

screen = Screen()  # 屏幕
screen.setup(width=600, height=600)  # 屏幕设置宽为600，高为600
screen.bgcolor("black")  # 设置屏幕的背景颜色为black
screen.title("My Snake Game")  # 将屏幕的标题设置为My Snake Game

'''
turtle.tracer(n=None, delay=None)
Parameters：
1. n – non-negative integer,如果给了n的值，则只有每n的时候screen才会update
2. delay – non-negative integer，设置延迟值

Turn turtle animation on/off and set delay for update drawings. 
If n is given, only each n-th regular screen update is really performed. 
(Can be used to accelerate the drawing of complex graphics.) 
When called without arguments, returns the currently stored value of n.
'''

screen.tracer(0)  # tracer的值设置为0

snake = Snake()
# food = Food()

screen.listen()  # 监听键盘的指令
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True  # 游戏是否继续
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()