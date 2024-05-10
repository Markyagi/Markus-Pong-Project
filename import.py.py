import turtle
import winsound
import random
import math
import time
import os

print('start')
# Set up the screen
wn = turtle.Screen()
wn.title("Pong by Markus")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.listen()
wn.tracer(1)

# Score
score_a = 0
score_b = 0

# Create the paddles
paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 10  # Increased ball speed
ball.dy = 10 # Increased ball speed
ball.angle = (-0.5, 0.5)
ball.delay = 0  # Delay before changing direction

score_left = turtle.Turtle()
score_left.speed(0)
score_left.penup()
score_left.hideturtle()
score_left.goto(-350, 250)
score_left.write("0", align="center", font=("Courier", 24, "normal"))

score_right = turtle.Turtle()
score_right.speed(0)
score_right.penup()
score_right.hideturtle()
score_right.goto(350, 250)
score_right.write("0", align="center", font=("Courier",24, "normal"))

power_up = turtle.Turtle()
power_up.speed(0)
power_up.shape("circle")
power_up.color("green")
power_up.shapesize(stretch_wid=0.5, stretch_len=0.5)
power_up.penup()
power_up.hideturtle()
power_up.goto(random.randint(-400, 400), 250)

# Initialize scores
score_left_value = 0
score_right_value = 0

# Game start/stop flag
game_started = True

def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Paddle A keys
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")

while True:
    wn.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1
        print('border collision - side')
    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        ball.dy *= -1
        time.sleep(1)
        print('border collision - top/bottom')
    
# Function to detect collisions between the ball and the paddles
    def ball_paddle_collision():
        if (ball.dx > 0):
            x = ball.xcor()
            y = ball.ycor()
            x -= 20
            y -= 20
        if (x < paddle_b_up.xcor() + 50 and x > paddle_b_up.xcor() - 50 and y < paddle_b_up.ycor() + 50 and y > paddle_b_up.ycor() - 50):
            ball.setx(-340)
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            
        elif (x > paddle_b_down.xcor() - 50 and x < paddle_b_down.xcor() + 50 and y < paddle_b_down.ycor() + 50 and y > paddle_b_down.ycor() - 50):
            ball.dx *= -1
            ball.dy *= random.uniform(-0.5, 0.5)
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

# Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)


    # Paddle collision
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            print('paddle left hit')
      
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
            ball.dx *= -1
            winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
            print('paddle right hit')
            
 
       
            
    
        