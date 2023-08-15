from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x = 5
        self.y = 5


    def move(self):
        nx = self.xcor() + self.x
        ny = self.ycor() + self.y
        self.goto(nx,ny)

    def hit_y_wall(self):
        self.y = self.y * (-1)

    def hit_user(self):
        self.x = self.x * (-1)

    def reset(self):
        self.goto(0,0)


