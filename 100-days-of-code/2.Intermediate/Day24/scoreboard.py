from turtle import Turtle, Screen
ALIGMENT = "center"
FONT = ("Arial", 24, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(x=0, y=260)
        self.score = 0
        with open("data.txt", "r") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        """Updating score and high score"""
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGMENT, font=FONT)

    def reset(self):
        """Reseting a scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt","w") as file:
                file.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        """Information about your score in your game."""
        self.score += 1
        self.clear()
        self.update_scoreboard()



