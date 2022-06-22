from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        # 也是老样子，我们使用turtle来创建一个桨
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    # 创建一个go_up函数
    def go_up(self):
        new_y = self.ycor() + 20  # y将会沿着y轴增加20
        self.goto(self.xcor(), new_y)  # 使用goto，然后保持xcor不便，y的值更新为new_y

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)