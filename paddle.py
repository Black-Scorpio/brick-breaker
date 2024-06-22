import turtle

class Paddle:
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("blue", "white")
        self.paddle.shapesize(stretch_wid=1, stretch_len=5)
        self.paddle.penup()
        self.paddle.goto(position)
        self.paddle.dx = 0

    def start_move_right(self):
        self.paddle.dx = 2

    def stop_move_right(self):
        if self.paddle.dx > 0:
            self.paddle.dx = 0

    def start_move_left(self):
        self.paddle.dx = -2

    def stop_move_left(self):
        if self.paddle.dx < 0:
            self.paddle.dx = 0

    def move(self):
        new_x = self.paddle.xcor() + self.paddle.dx
        if -450 < new_x < 450:
            self.paddle.setx(new_x)
