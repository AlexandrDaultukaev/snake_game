from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake = []
        for i in range(3):
            self.snake.append(Turtle())
            self.snake[i].penup()
            self.snake[i].shape("square")
            self.snake[i].color("white")
            self.snake[i].goto(20 * i, 0)
        self.head = self.snake[len(self.snake) - 1]

    def add_segment(self):
        """
        Activated when snake ate food
        """
        self.snake.insert(0, Turtle())
        self.snake[0].penup()
        self.snake[0].shape("square")
        self.snake[0].color("white")
        self.snake[0].setpos(self.snake[1].position())

    def move(self):
        """
        Moves all segments of the snake
        """
        for segment in range(len(self.snake)):
            if segment == len(self.snake) - 1:
                self.snake[segment].forward(20)
            else:
                self.snake[segment].goto(self.snake[segment + 1].pos())

    def move_up(self):
        if self.head.heading() == 270:
            return
        self.head.setheading(90)

    def move_right(self):
        if self.head.heading() == 180:
            return
        self.head.setheading(0)

    def move_left(self):
        if self.head.heading() == 0:
            return
        self.head.setheading(180)

    def move_down(self):
        if self.head.heading() == 90:
            return
        self.head.setheading(270)