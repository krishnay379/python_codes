import time
from turtle import Turtle,Screen
from player import Player
from carmanager import CarManager
from scoreboard import Scoreboard

player = Player()
screen = Screen()
carmanager = CarManager()
scoreboard = Scoreboard()


screen.setup(width = 600 , height = 600)
screen.tracer(0)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    carmanager.create_car()
    carmanager.move_cars()

    #  detect colision with car
    for car in carmanager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        carmanager.increase_speed()
        scoreboard.increase_level()
    screen.listen()
    screen.onkey(player.move,"Up")
screen.exitonclick()

