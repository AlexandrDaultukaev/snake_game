from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.setpos(0, 280)
        self.set_score()

    def set_score(self):
        self.write(f"Score = {self.score}", False, align="center", font=("Arial", 10, "italic"))
