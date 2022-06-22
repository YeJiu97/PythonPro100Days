import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()

player = Player()
car_manager = CarManager()


screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_cars()
    car_manager.move_cars()

    # 检测是否失败
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on == False
            screen.title("You Lost")
            time.sleep(0.5)
            player.go_to_start()

    # 检测是否成功
    if player.is_at_finish_line():
        screen.title("You Win")
        time.sleep(0.5)
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()