from turtle import Turtle, Screen
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        """Reseting a scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     """Informaction when you finish the game."""
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER ", align=ALIGMENT, font=FONT)

    def increase_score(self):
        """Information about your score in your game."""
        self.score += 1
        self.clear()
        self.update_scoreboard()



