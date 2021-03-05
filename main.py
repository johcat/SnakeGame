from turtle import Screen
import time
import snake
from food import Food
from scoreboard import ScoreBoard

SPEED = 0.2

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Asma's Snake Game")

snake = snake.Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    snake.move()
    screen.update()
    time.sleep(SPEED)

    if snake.snakes[0].distance(food) < 15:
        food.refresh()
        scoreboard.update_score()
        snake.add_snake()

    if snake.snakes[0].xcor() > 290 or snake.snakes[0].xcor() < -290 or snake.snakes[0].ycor() > 290 or snake.snakes[0].ycor() < -290:
        game_is_on = False
        scoreboard.game_over()

    for creatures in snake.snakes[1:]:
        if snake.snakes[0].distance(creatures) < 10:
            game_is_on = False
            scoreboard.game_over()





screen.exitonclick()