from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 18, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.display_score()

    def display_score(self):
        self.goto(0, 240)
        self.write(f"Score: {self.score}", True, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER.", True, align=ALIGNMENT, font=FONT)
