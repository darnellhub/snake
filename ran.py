from turtle import Turtle
import random


# car_lanes = [(160,0),(140,0), (120,0), (100,0)]
car_lanes = [140, 100, 60, 20, -20, -60, -100, -140]
random_colours = ["red", "orange", "pink", "blue", "purple", "yellow"]

for lanes in range(len(car_lanes)):
    x_lanes = random.choice(car_lanes)


all_cars=[]




def create_car():
    new_car = Turtle("square")
    new_car.penup()
    new_car.color("red")
    new_car.shapesize(stretch_wid=1, stretch_len=3)
    random_l = random.randrange(len(car_lanes))
    random_lane = car_lanes[random_l]
    turtle.goto(0, random_lane)
    all_cars.append(new_car)

create_car()
print(all_cars)