from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.randX = random.randint(-280, 280)
        self.randY = random.randint(-280, 280)
        self.setpos(self.randX, self.randY)

