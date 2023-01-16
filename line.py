from turtle import Turtle


class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -300)
        self.setheading(90)
        self.draw()

    def draw(self):
        for _ in range(60):
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)