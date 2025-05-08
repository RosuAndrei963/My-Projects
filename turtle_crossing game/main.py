import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    player.is_at_finish()

    for the_car in car.all_cars:  # check collision with cars
        if player.distance(the_car) < 22:
            scoreboard.game_over()
            game_on = False


    if player.is_at_finish():  # check for finish line
        player.goto_start()
        car.increase_speed()
        scoreboard.increase_level()


screen.exitonclick()