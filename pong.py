import imp
from multiprocessing.connection import wait
from pdb import Restart
from sqlite3 import Time


import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

#score
score1 = 0
score2 = 0

#paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)
#paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)
#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.15
ball.dy = -0.15
#score
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0   Player B: 0", align="center", font=("Courier", 24, "normal"))

#function
def paddle_1_up():
    y = paddle_1.ycor()
    y += 20
    paddle_1.sety(y)
def paddle_1_down():
    y = paddle_1.ycor()
    y -= 20
    paddle_1.sety(y)
def paddle_2_up():
    y2 = paddle_2.ycor()
    y2 += 20
    paddle_2.sety(y2)
def paddle_2_down():
    y2 = paddle_2.ycor()
    y2 -= 20
    paddle_2.sety(y2)

#keyboard
wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

# main loop
while True:
    wn.update()
    #move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    

    #border check
    if ball.ycor() > 290:
        ball.dy *= -1 
    if ball.ycor() < -290:
        ball.dy *= -1
    if  ball.xcor() > 390:
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
    if  ball.xcor() < -390:
        ball.dx *= -1
        ball.goto(0, 0)
        score2 += 1
        pen.clear()
        pen.write("Player A: {}   Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))
        #paddle collide
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 40 and ball.ycor() > paddle_2.ycor() - 40):
        ball.dx *= -1
        ball.setx(330)
    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 40 and ball.ycor() > paddle_1.ycor() - 40):
        ball.dx *= -1
        ball.setx(-330)

