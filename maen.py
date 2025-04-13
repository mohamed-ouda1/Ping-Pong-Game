from turtle import Screen
import time
from paddle import Paddle
screen=Screen()
screen.setup(1000,800)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)
from score import Score
from ball import Ball
ball=Ball()
paddle1= Paddle(450)
paddle2=Paddle(-450)
score=Score()
score.score_pord()
screen.listen()
screen.onkey(paddle1.move_up,"Up")
screen.onkey(paddle1.move_down,"Down")
screen.onkey(paddle2.move_up,"w")
screen.onkey(paddle2.move_down,"s")
while True:
    screen.update()
    time.sleep(.1)
    ball.move()
    if ball.ycor() >= 380 or ball.ycor() <= -380 :
       ball.me_y *=-1

    if (  ball.xcor() >=430  and ball.distance(paddle1) <= 50 ) or (  ball.xcor()<=-430 and ball.distance(paddle2)<=50 )  :
       ball.me_x *=-1
       ball.me_x +=0.5
       ball.me_y +=0.5

    if ball.xcor() >=500  :
       score.updat_1()
       ball.again()

    elif ball.xcor() <= -500 :
        score.updat_2()
        ball.again()


    
screen.exitonclick()