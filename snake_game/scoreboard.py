"""ScoreBoard module"""
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class ScoreBoard(Turtle):
    """ScoreBoard"""

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", encoding="utf8") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update socre board"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        """reset"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w", encoding="utf8") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Increase score"""
        self.score += 1
        self.update_scoreboard()
