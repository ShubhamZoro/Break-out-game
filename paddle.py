from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.goto(position)
        self.tilt(90)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5,stretch_len=1)

    def right_mov(self):

        r = self.xcor()+20
        self.goto(r,self.ycor())

    def left_mov(self):

        r = self.xcor() - 20
        self.goto(r, self.ycor())