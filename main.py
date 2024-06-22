import turtle
from game import BreakMyBricks

# Set up the screen
wn = turtle.Screen()
wn.title("Break My Bricks")
wn.bgcolor("black")
wn.setup(width=1000, height=800)
wn.tracer(0)

# Initialize game
game = BreakMyBricks(wn)

# Keyboard bindings
wn.listen()
wn.onkeypress(game.start_game, "s")
wn.onkeypress(game.paddle.start_move_right, "Right")
wn.onkeyrelease(game.paddle.stop_move_right, "Right")
wn.onkeypress(game.paddle.start_move_left, "Left")
wn.onkeyrelease(game.paddle.stop_move_left, "Left")
wn.onkeypress(game.paddle.start_move_right, "d")
wn.onkeyrelease(game.paddle.stop_move_right, "d")
wn.onkeypress(game.paddle.start_move_left, "a")
wn.onkeyrelease(game.paddle.stop_move_left, "a")
wn.onkeypress(game.start_ball, "space")
wn.onkeypress(game.next_level, "n")
wn.onkeypress(game.quit_game, "q")

# Main game loop
while True:
    wn.update()
    game.update()
