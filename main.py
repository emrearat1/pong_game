from turtle import Turtle, Screen
from users import Users
from ball import Ball
import time
screen = Screen()
screen.bgcolor("yellow")
screen.setup(width=1000, height=800)
screen.title("pong game")

screen.tracer(0)

user1 = Users((-450, 0))
user2 = Users((450, 0))
ball = Ball()

screen.listen()
screen.onkey(user1.go_up, "w")
screen.onkey(user1.go_down, "s")
screen.onkey(user2.go_up, "Up")
screen.onkey(user2.go_down, "Down")


check = True

while check:
    time.sleep(0.05)
    ball.move()
    screen.update()

    if ball.ycor() > 380 or ball.ycor()<-380:
        ball.hit_y_wall()

    if ball.distance(user2) < 30 or ball.distance(user1) < 30:
        ball.hit_user()
    if ball.xcor() > 480 or ball.xcor() < -480 :
        ball.reset()
        ball.hit_user()

screen.exitonclick()

