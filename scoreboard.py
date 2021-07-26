from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "italic")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.ht()
        self.penup()
        self.setpos(0, 280)
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.setpos(0, 0)
        self.write(f"GAME OVER", False, align=ALIGNMENT, font=FONT)
