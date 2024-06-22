import turtle
import random
from paddle import Paddle
from ball import Ball
from brick import Brick
from user_score import UserScore


class BreakMyBricks:
    def __init__(self, wn):
        self.wn = wn
        self.user_score = UserScore()
        self.highest_score = 0
        self.paddle = Paddle((0, -350))
        self.ball = Ball(self.paddle)
        self.bricks = []
        self.score_display = turtle.Turtle()
        self.score_display.speed(0)
        self.score_display.color("white")
        self.score_display.penup()
        self.score_display.hideturtle()
        self.score_display.goto(-450, 360)

        self.high_score_display = turtle.Turtle()
        self.high_score_display.speed(0)
        self.high_score_display.color("white")
        self.high_score_display.penup()
        self.high_score_display.hideturtle()
        self.high_score_display.goto(450, 360)

        self.title_display = turtle.Turtle()
        self.title_display.speed(0)
        self.title_display.color("white")
        self.title_display.penup()
        self.title_display.hideturtle()
        self.title_display.goto(0, 0)
        self.title_display.write("Break My Bricks", align="center", font=("Courier", 36, "normal"))
        self.title_display.goto(0, -40)
        self.title_display.write("Press 's' to start", align="center", font=("Courier", 24, "normal"))

        self.level_cleared_display = turtle.Turtle()
        self.level_cleared_display.speed(0)
        self.level_cleared_display.color("white")
        self.level_cleared_display.penup()
        self.level_cleared_display.hideturtle()

        self.game_state = "start"
        self.ball_in_play = False

        # Keyboard bindings
        self.wn.listen()
        self.wn.onkeypress(self.start_game, "s")
        self.wn.onkeypress(self.start_ball, "space")
        self.wn.onkeypress(self.next_level, "n")
        self.wn.onkeypress(self.quit_game, "q")

    def create_bricks(self):
        self.bricks.clear()  # Clear the bricks list before creating new bricks
        for y in range(1):
            for x in range(-450, 450, 100):
                brick = Brick((x, 300 - y * 50), 1, "green")
                self.bricks.append(brick)

    def start_game(self):
        if self.game_state not in ["start", "game_over"]:
            return
        self.game_state = "playing"
        self.ball_in_play = False
        self.title_display.clear()
        self.user_score.reset()
        self.remove_all_bricks()
        self.create_bricks()
        self.ball.reset_position(self.paddle)
        self.update_score_display()

    def next_level(self):
        if self.game_state != "level_cleared":
            return
        self.user_score.level += 1
        self.game_state = "playing"
        self.ball_in_play = False
        self.level_cleared_display.clear()
        self.create_bricks()
        self.ball.increase_speed(self.user_score.level)
        self.ball.reset_position(self.paddle)

    def remove_all_bricks(self):
        for brick in self.bricks:
            brick.destroy()
        self.bricks.clear()

    def game_over(self):
        self.game_state = "game_over"
        self.score_display.goto(0, 0)
        self.score_display.write("Game Over", align="center", font=("Courier", 36, "normal"))
        self.score_display.goto(0, -40)
        self.score_display.write(f"Your Score: {self.user_score.score}", align="center", font=("Courier", 24, "normal"))
        if self.user_score.score > self.highest_score:
            self.highest_score = self.user_score.score
            self.score_display.goto(0, 80)
            self.score_display.write(f"Wow You've Got a New High Score!! {self.user_score.score}", align="center", font=("Courier", 24, "normal"))
        self.score_display.goto(0, -120)
        self.score_display.write("Press 's' to start over\nPress 'q' to quit", align="center", font=("Courier", 18, "normal"))

    def level_cleared(self):
        self.game_state = "level_cleared"
        self.level_cleared_display.goto(0, 0)
        self.level_cleared_display.write("Level Cleared", align="center", font=("Courier", 36, "normal"))
        self.level_cleared_display.goto(0, -40)
        self.level_cleared_display.write("You Win", align="center", font=("Courier", 24, "normal"))
        self.level_cleared_display.goto(0, -80)
        self.level_cleared_display.write("Press 'n' to go to the next level", align="center", font=("Courier", 24, "normal"))

    def start_ball(self):
        if not self.ball_in_play and self.game_state == "playing":
            self.ball_in_play = True
            self.ball.shoot()

    def quit_game(self):
        self.game_state = "quit"
        self.wn.bye()

    def update(self):
        if self.game_state == "playing":
            # Move the paddle
            self.paddle.move()

            # Move the ball
            if self.ball_in_play:
                self.ball.move()
            else:
                self.ball.follow_paddle(self.paddle)

            # Border checking
            if self.ball.ball.xcor() > 490 or self.ball.ball.xcor() < -490:
                self.ball.bounce_x()

            if self.ball.ball.ycor() > 390:
                self.ball.bounce_y()

            if self.ball.ball.ycor() < -390:
                self.ball_in_play = False
                self.user_score.lose_life()
                self.ball.reset_position(self.paddle)

            # Paddle and ball collisions
            if (self.ball.ball.ycor() > -340 and self.ball.ball.ycor() < -330) and (
                    self.paddle.paddle.xcor() - 50 < self.ball.ball.xcor() < self.paddle.paddle.xcor() + 50):
                self.ball.bounce_y()

            # Ball and brick collisions
            for brick in self.bricks:
                if self.ball.ball.distance(brick.brick) < 45:
                    # Get the coordinates of the ball and brick
                    ball_x, ball_y = self.ball.ball.xcor(), self.ball.ball.ycor()
                    brick_x, brick_y = brick.brick.xcor(), brick.brick.ycor()

                    # Determine the collision direction
                    if abs(ball_y - brick_y) < 10 and (
                            brick_x - 50 < ball_x < brick_x + 50):  # Top and bottom collision
                        self.ball.bounce_y()
                    elif abs(ball_x - brick_x) < 20 and (brick_y - 20 < ball_y < brick_y + 20):  # Side collision
                        self.ball.bounce_x()
                    else:
                        self.ball.bounce_y()  # Default to bouncing in the y direction if ambiguous

                    brick.destroy()
                    self.bricks.remove(brick)
                    self.user_score.increase_score()
                    break

            # Check for level cleared
            all_bricks_cleared = all(not brick.brick.isvisible() for brick in self.bricks)
            if all_bricks_cleared:
                if self.user_score.score > self.highest_score:
                    self.highest_score = self.user_score.score
                self.level_cleared()

            # Update the score display
            self.update_score_display()

            # Check for game over
            if self.user_score.lives == 0:
                self.game_over()

        elif self.game_state == "game_over":
            self.wn.onkeypress(self.start_game, "s")
            self.wn.onkeypress(self.quit_game, "q")

        elif self.game_state == "level_cleared":
            self.wn.onkeypress(self.next_level, "n")

    def update_score_display(self):
        self.score_display.clear()
        self.score_display.goto(-450, 360)
        self.score_display.write(
            f"Score: {self.user_score.score}  Lives: {self.user_score.display_lives()}  Level: {self.user_score.level}",
            align="left", font=("Courier", 18, "normal"))
        self.high_score_display.clear()
        self.high_score_display.goto(450, 360)
        self.high_score_display.write(f"Highest Score: {self.highest_score}", align="right",
                                      font=("Courier", 18, "normal"))
