
import turtle
import winsound

wn = turtle.Screen()
wn.title("Ping - Pong")
wn.bgcolor("green")
wn.setup(width=800, height=600)
wn.tracer(0)

#CenterLine
center = turtle.Turtle()
center.speed(0)
center.shape("square")
center.shapesize(stretch_wid=100,stretch_len=0.1)
center.color("white")
center.penup()
center.goto(0,0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=6,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-350, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=6,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(350,0)

# Ball 
ball = turtle.Turtle()

ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4
#Score 
score1 = 0
score2 = 0
#Pen-Score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player1: 0 Player2: 0",align="center" , font=("Arial",20, "bold"))


# Functions 

# Paddle A movement
def paddle_aUp():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_aDown():
    y=paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
# Paddel B movement
def paddle_bUp():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_bDown():
    y=paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keyboard inputs
wn.listen()

wn.onkeypress(paddle_aUp,"w")
wn.onkeypress(paddle_aDown,"s")

wn.onkeypress(paddle_bUp,"Up")
wn.onkeypress(paddle_bDown,"Down")


while True:
    wn.update()

    #Move the ball

    ball.setx(ball.xcor()+ ball.dx)
    ball.sety(ball.ycor()+ ball.dy)

    #Border Check

    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *=-1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *=-1
    
    if ball.xcor() > 390:
        ball.goto (0,0)
        ball.dx *= -1
        score2 += 1
        winsound.Beep(150,100)
        pen.clear()
        pen.write("Player1: {} Player2: {}".format(score1,score2),align="center" , font=("Arial",20, "bold"))
    
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score1 += 1
        winsound.Beep(150,100)
        pen.clear()
        pen.write("Player1: {} Player2: {}".format(score1,score2),align="center" , font=("Arial",20, "bold"))

    #Paddel and Ball Collisions

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        winsound.PlaySound("Ball_Bounce-Popup_Pixels-172648817.wav" , winsound.SND_ASYNC)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        winsound.PlaySound("Ball_Bounce-Popup_Pixels-172648817.wav", winsound.SND_ASYNC)
        ball.dx *= -1
    
