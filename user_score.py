class UserScore:
    def __init__(self):
        self.score = 0
        self.lives = 5
        self.level = 1

    def increase_score(self):
        self.score += 50

    def lose_life(self):
        self.lives -= 1

    def reset(self):
        self.score = 0
        self.lives = 5
        self.level = 1

    def display_lives(self):
        hearts = "♥" * self.lives + "♡" * (5 - self.lives)
        return hearts

    def display(self):
        hearts = "♥" * self.lives + "♡" * (5 - self.lives)
        return f"Score: {self.score}  Lives: {hearts}  Level: {self.level}"
