from turtle import Turtle
import random
colors = ["sky blue", "tomato", "lime green","yellow"]
index = random.randint(0,len(colors)-1)

class Brick():
    def __init__(self):
        self.row = []

    def makeRow(self):
        index = random.randint(0, len(colors) - 1)

        y=250
        for j in range(4):
            x = -350
            for i in range(12):
                targetT = Turtle()
                targetT.speed(0)
                targetT.shape("square")
                targetT.shapesize(stretch_len=3,stretch_wid=1)
                targetT.color(colors[index])
                targetT.penup()
                targetT.goto(x + 60 * i+i*2, y)
                targetT.pendown()
                self.row.append(targetT)
                index = random.randint(0, len(colors) - 1)
            y=y-30




