import time
from turtle import Screen
from snake import Snake
from food import Food
from bg import Bg
from score import Score

background = Bg()
snake = Snake()
screen = Screen()
food = Food()
score = Score()

"""Create background"""
background.create_background()
"""Move Snake"""
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    """Eating Food"""
    if snake.head.distance(food) < 15:
        food.move_food()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() > 380 or snake.head.xcor() < -380 or snake.head.ycor() > 380 or snake.head.ycor() < -380:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:

            score.reset()
            snake.reset()
            # game_is_on = False
            # score.game_over()


screen.exitonclick()