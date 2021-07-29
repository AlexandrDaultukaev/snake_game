import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Screen customization
sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.listen()
sc.tracer(0)



snake = Snake()

food = Food()

# Event handlers
sc.onkey(snake.move_left, "Left")
sc.onkey(snake.move_right, "Right")
sc.onkey(snake.move_down, "Down")
sc.onkey(snake.move_up, "Up")


score = ScoreBoard()


sc.update()
game_is_on = True
while game_is_on:
    with open("data.txt") as file:
        score.high_score = int(file.read())
        score.update_scoreboard()
    sc.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) <= 15:
        snake.add_segment()
        score.increase_score()
        food.refresh()

    # Detect collision with wall
    for i in range(2):
        # probably snake.head.position()[i]**2 > 280**2 would be better(for brevity)
        # probably snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280
        # would be faster
        if snake.head.position()[i] > 280 or snake.head.position()[i] < -280:
            score.reset()
            with open("data.txt", "w") as file:
                file.write(str(score.high_score))
            snake.start_position()

    # Detect collision with tail
    for segment in snake.snake[0: len(snake.snake) - 1]:
        if snake.head.distance(segment) < 10:
            score.reset()
            with open("data.txt", "w") as file:
                file.write(str(score.high_score))
            snake.start_position()
    sc.update()

sc.exitonclick()
