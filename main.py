import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game. Score 0")
sc.listen()
sc.tracer(0)
score = 0
snake = Snake()

# print(f"Size: {snake[1].turtlesize()}")
food = Food()


sc.onkey(snake.move_left, "Left")
sc.onkey(snake.move_right, "Right")
sc.onkey(snake.move_down, "Down")
sc.onkey(snake.move_up, "Up")

sc.update()
game_is_on = True
while game_is_on:
    sc.update()
    snake.move()
    if snake.head.distance(food) <= 15:
        score += 1
        sc.title(f"Snake Game. Score {score}")
        food.refresh()
    time.sleep(0.1)
    sc.update()










sc.exitonclick()