"""Score board module"""
from turtle import Turtle

FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    """score board"""

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)
        self.update_scoreboard()

    def update_scoreboard(self):
        """update score board"""
        self.clear()
        self.write(f"level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        """increase level"""
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        """game over"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)
