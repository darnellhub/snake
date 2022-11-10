from turtle import Screen
WIDTH = 800
HEIGHT = 800
class Bg:
    def __init__(self):
        self.screen = Screen()
        self.create_background()
    def create_background(self):
        self.screen.setup(WIDTH, HEIGHT)
        self.screen.title("Feeding Anaconda")
        self.screen.bgcolor("black")
        self.screen.tracer(0)