from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 10, "italic")


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.ht()
        self.penup()
        self.setpos(0, 280)
        self.write(f"Score = {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score} High score: {self.high_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        with open("data.txt", "w") as file:
            file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def goodbye(self):
        self.goto(0, 0)
        self.write("Goodbye!", False, align=ALIGNMENT, font=FONT)
