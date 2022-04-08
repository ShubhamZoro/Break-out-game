from turtle import Screen

from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from block import Brick

import time
screen=Screen()
screen.tracer(0)
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Breakout game")
score=Scoreboard()
ball=Ball()
paddle=Paddle((-300,-260))
screen.listen()
screen.onkeypress(paddle.right_mov,"Right")
screen.onkeypress(paddle.left_mov,"Left")

bricks=Brick()
bricks.makeRow()
screen.update()
is_on=True


while is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    for brick in bricks.row:
        if ball.distance(brick)<33:
            brick.penup()
            brick.goto(1000,1000)
            ball.bounce_y()
            score.scores()

    if ball.xcor()>380 or ball.xcor()<-380:
        ball.bounce_x()

    #to detect collision with the r_paddle
    if ball.distance(paddle)<33 and ball.ycor()<-240:
        ball.bounce_y()

    if ball.ycor()>288:
        ball.bounce_y()


    if ball.ycor()<-288:
        is_on = False

        score.result("You lose")


    if score.score==10:
        is_on = False
        score.result("You win")

        # Turtle.write("You Win", align="center",font= ('Courier', 30, 'italic'))

screen.mainloop()
