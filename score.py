from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Score (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 370)
        self.update_score()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.read_highscore()}", align=ALIGNMENT, font=FONT)


    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        # self.clear()
        if self.score > self.read_highscore():
            self.save_file()
        self.clear()
        self.score = 0
        self.update_score()


    def increase_score(self):
        # self.clear()
        self.score += 1
        self.update_score()

    def save_file(self):
        with open("data.txt", "w") as file:
            scores = str(self.score)
            file.write(scores)

    def read_highscore(self):
        with open("data.txt", "r") as file:
            score = int(file.read())
            return score






