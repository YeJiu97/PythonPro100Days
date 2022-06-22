from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# 还是老样子，弄一个screen出来
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong-game")
screen.tracer(0)  # 在这里现将屏幕关闭了

# 调用paddle类来生成左右两个paddles
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# 接着是生成ball
ball = Ball()

# 显示分数板
scoreboard = Scoreboard()

# 让屏幕进行监听
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

# while循环
game_is_on = True
while game_is_on:
    time.sleep(0.05)  # 每0.1秒刷新一次
    screen.update()  # 到了这里才会对屏幕进行更新
    ball.move()

    # 检测撞墙
    if ball.ycor() > 280 or ball.ycor() < -280:
        # 需要进行反射
        ball.bounce_y()

    # 检查ball和paddle之间的关系
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # 一方miss
    if ball.xcor() > 380:
        time.sleep(1)  # 停顿一下，然后从0，0开始进行反方向运动
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        time.sleep(1)
        ball.reset_position()
        scoreboard.r_point()


# 直到点击才能够退出
screen.exitonclick()