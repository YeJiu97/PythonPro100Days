import turtle as t

tim = t.Turtle()

for _ in range(4):

    for _ in range(15):
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

    tim.left(90)

my_screen = t.Screen()
my_screen.exitonclick()
