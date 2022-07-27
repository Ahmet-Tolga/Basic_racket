import turtle
import time
pen=turtle.Screen()
pen.bgcolor("black")
pen.setup(height=600,width=1000)

raket=turtle.Turtle()
raket.color("gold")
raket.shape("square")
raket.shapesize(1,5)
raket.penup()
raket.goto(0,-250)
raket.speed(0)

ball=turtle.Turtle()
ball.color("silver")
ball.shape("circle")
ball.speed(0)
ball.goto(0,0)
ball.penup()
puan=0
yaz=turtle.Turtle()
yaz.speed(0)
yaz.color("white")
yaz.penup()
yaz.goto(0,260)
yaz.hideturtle()
yaz.write("puan:{}".format(puan),align="center",font=("courier",24,"normal"))
x=5
y=5
def f():
    y=20
    x=raket.xcor()
    raket.setx(raket.xcor()+y)
def g():
    y=20
    x=raket.xcor()
    raket.setx(raket.xcor()-y)

pen.listen()
pen.onkeypress(f,"Right")
pen.onkeypress(g,"Left")
a=0
while True:
    pen.update()
    ball.setx(ball.xcor()+x)
    ball.sety(ball.ycor()+y)
    if ball.ycor()>290:
        y*=(-1)
    if ball.ycor()<-290:
        ball.goto(0,0)
        x*=(-1)
        a+=1
    if ball.xcor()>490 or ball.xcor()<-490:
        x*=(-1)
    if (ball.xcor()<raket.xcor()+50 and ball.xcor()>raket.xcor()-50) and (ball.ycor()<-250 and ball.ycor()>-260):
        y*=(-1)
        x*=(-1)
        puan += 10
        yaz.clear()
        yaz.write("puan:{}".format(puan),align="center",font=("courier",24,"normal"))
    if a==3:
        pen.bgcolor("white")
        pen.bgcolor("black")
        puan=0
        yaz.clear()
        yaz.write("puan:{}".format(puan), align="center", font=("courier", 24, "normal"))
        x=0
        y=0


