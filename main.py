import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard


sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.listen()
sc.tracer(0)
score = 0
snake = Snake()

food = Food()


sc.onkey(snake.move_left, "Left")
sc.onkey(snake.move_right, "Right")
sc.onkey(snake.move_down, "Down")
sc.onkey(snake.move_up, "Up")
score = ScoreBoard()
sc.update()
game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) <= 15:
        snake.add_segment()
        score.increase_score()
        food.refresh()

    for i in range(2):
        # probably snake.head.position()[i]**2 > 280**2 would be better(for brevity)
        # probably snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280
        # would be faster
        if snake.head.position()[i] > 280 or snake.head.position()[i] < -280:
            score.game_over()
            game_is_on = False

        for segment in snake.snake:
            if segment == snake.head:
                pass
            elif snake.head.distance(segment) < 10:
                score.game_over()
                game_is_on = False







sc.exitonclick()