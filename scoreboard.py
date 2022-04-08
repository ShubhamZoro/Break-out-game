from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.score=0
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, -200)
        self.write(self.score, align="center", font=("Arial", 60, "normal"))

    def scores(self):
        self.score+=1
        self.update_scoreboard()

    def result(self, text):
        self.goto(0, 0)
        self.write(text, align="center",font= ('Courier', 30, 'italic'))




