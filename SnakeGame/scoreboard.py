from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # TODO: Reading the data file1.txt for HighScore
        with open("HighScore_data.txt") as data:
            self.High_score = int(data.read())

        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.display_score()

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.High_score}", align = ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.High_score:
            self.High_score = self.score
        self.score = 0
        self.display_score()
        # Write new high score into file1.txt
        with open("HighScore_data.txt", "w") as data:
            data.write(str(self.High_score))

    def increase_score(self):
        self.score += 1
        self.display_score()
