from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = -1
        self.update_score()

    def update_score(self):
        self.score += 1
        self.reset()
        self.penup()
        self.hideturtle()
        self.goto(0, 280)
        self.color("white")
        self.write(f"Asma's score: {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.write("GAME OVER - BETTER LUCK NEXT TIME, ASMA", align="center", font=("Arial", 15, "normal"))