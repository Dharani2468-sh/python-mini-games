from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 25, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-20, 270)
        self.update_score()

    def update_score(self):
        self.goto(-100, 250)
        self.write(self.l_score, align = ALIGNMENT, font=FONT)
        self.goto(100, 250)
        self.write(self.r_score, align = ALIGNMENT, font=FONT)

    def l_score(self):
        self.l_score += 1
        self.update_score()

    def r_score(self):
        self.r_score += 1
        self.update_score()


