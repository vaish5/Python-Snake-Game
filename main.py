from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
# screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("🐍 Classic Snake Game 🐍")
screen.tracer(0)
screen.setup(width=1.0, height=1.0)
screen_height = screen.window_height()
screen_width = screen.window_width()

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if (snake.head.xcor() > (screen_width/2)-20 or snake.head.xcor() < -((screen_width/2)-20) or
            snake.head.ycor() > (screen_height/2)-20 or snake.head.ycor() < -((screen_height/2)-20)):
        game_is_on = False
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()
