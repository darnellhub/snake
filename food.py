from turtle import Turtle
import random


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.move_food()

    def move_food(self):
        random_x_cor = random.randint(-280, 280)
        random_y_cor = random.randint(-280, 280)
        self.goto(random_x_cor, random_x_cor)