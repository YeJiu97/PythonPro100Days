from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        # self.goto(STARTING_POSITION)
        self.go_to_start()
        self.setheading(90)  # 默认的情况之下，头朝上

    # 进行方向性的移动，但是需要调转方向
    def go_up(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def go_down(self):
        self.setheading(270)
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
