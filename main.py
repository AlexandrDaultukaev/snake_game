import time
from turtle import Turtle, Screen
sc = Screen()
sc.setup(width=600, height=600)
sc.bgcolor("black")
sc.title("Snake Game")
# sc.listen()
snake = []
sc.tracer(0)


def init_snake(tail):
    for i in range(3):
        snake.append(Turtle())
        snake[i].penup()
        snake[i].shape("square")
        snake[i].color("white")
        snake[i].goto(20 * i, 0)

# print(f"Size: {snake[1].turtlesize()}")

# def move_forward():
#     snake[len(snake)-1].forward(20)
#
# def move_left():
#     snake[len(snake) - 1].left(90)
#     snake[len(snake) - 1].forward(20)
#
# def move_right():
#     snake[len(snake) - 1].right(90)
#     snake[len(snake) - 1].forward(20)


sc.update()
init_snake(3)
game_is_on = True
while game_is_on:
    sc.update()
    time.sleep(0.1)
    for segment in range(len(snake)):
        if segment == len(snake) - 1:
            snake[segment].forward(20)
            # sc.onkey(move_forward, "w")
            # sc.onkey(move_left, "a")
            # sc.onkey(move_forward, "d")
        else:
            snake[segment].goto(snake[segment+1].pos())








sc.exitonclick()