from turtle import Turtle, Screen


class Users(Turtle):
    def __init__(self, cordinates):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=1)
        self.penup()
        self.goto(cordinates)

    def go_up(self):
        ny = self.ycor() + 20
        self.goto(self.xcor(), ny)
    def go_down(self):
        ny = self.ycor() - 20
        self.goto(self.xcor(), ny)
