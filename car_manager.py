import random
from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 3


class CarManager:
     def __init__(self):
         self.cars=[]
         self.car_speed=STARTING_MOVE_DISTANCE
     def create_car(self):
         chance=random.randint(1,6)
         if chance==1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            car_y = random.randint(-250, 250)
            new_car.goto(300, car_y)
            self.cars.append(new_car)


     def car_move(self):
       for car in self.cars:
           car.backward(self.car_speed)
     def level_up(self):
         self.car_speed+=MOVE_INCREMENT

