import turtle
import random

class Ball:
    def __init__(self, paddle):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("red")
        self.ball.penup()
        self.reset_position(paddle)
        self.base_speed = 0.8
        self.speed_multiplier = 1
        self.ball.dx = 0
        self.ball.dy = 0

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_x(self):
        self.ball.dx *= -1

    def bounce_y(self):
        self.ball.dy *= -1

    def reset_position(self, paddle):
        self.ball.goto(paddle.paddle.xcor(), paddle.paddle.ycor() + 20)
        self.ball.dx = 0
        self.ball.dy = 0

    def shoot(self):
        self.ball.dx = self.base_speed * self.speed_multiplier
        self.ball.dy = self.base_speed * self.speed_multiplier

    def follow_paddle(self, paddle):
        self.ball.setx(paddle.paddle.xcor())

    def increase_speed(self, level):
        self.base_speed = 1 + (level - 1) * 0.5
