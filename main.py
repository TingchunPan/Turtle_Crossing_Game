import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
FINISH_LINE_Y = 280
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player=Player()
car_manager=CarManager()
screen.onkey(player.move,"Up")
screen.listen()
screen.title("Turtle Crosing Game")

scoreboard=Scoreboard()
scoreboard.update_score()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    #detect collision with the car
    for car in car_manager.cars:
        if car.distance(player) <20:
            game_is_on=False
            scoreboard.game_over()
    #detect successful crossing
    if player.ycor()>FINISH_LINE_Y:
        player.return_origin()
        car_manager.level_up()
        scoreboard.increase_score()
        scoreboard.update_score()
screen.exitonclick()
