import turtle

class Brick:
    def __init__(self, position, hit_points, color):
        self.initial_position = position
        self.initial_hit_points = hit_points
        self.hit_points = hit_points
        self.color = color
        self.brick = turtle.Turtle()
        self.brick.speed(0)
        self.brick.shape("square")
        self.brick.color(self.color)
        self.brick.shapesize(stretch_wid=1, stretch_len=4)
        self.brick.penup()
        self.brick.goto(position)

    def hit(self):
        self.hit_points -= 1
        if self.hit_points <= 0:
            self.destroy()

    def destroy(self):
        self.brick.hideturtle()  # Hide the brick
        self.brick.clear()  # Clear the drawing (if any)
        self.brick.goto(1000, 1000)  # Move the brick off-screen
        self.brick.penup()  # Ensure it's not drawing

    def reset(self):
        self.brick.goto(self.initial_position)
        self.hit_points = self.initial_hit_points
        self.brick.color(self.color)
        self.brick.showturtle()  # Show the brick
