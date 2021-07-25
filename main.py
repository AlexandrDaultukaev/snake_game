import time
from turtle import Turtle, Screen
from snake import Snake
sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
sc.listen()
sc.tracer(0)

snake = Snake()

# print(f"Size: {snake[1].turtlesize()}")


sc.onkey(snake.move_left, "Left")
sc.onkey(snake.move_right, "Right")
sc.onkey(snake.move_down, "Down")
sc.onkey(snake.move_up, "Up")

sc.update()
game_is_on = True
while game_is_on:
    sc.update()
    snake.move()
    time.sleep(0.1)
    sc.update()










sc.exitonclick()