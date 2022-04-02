from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(x=0, y=260)
        self.color("white")
        self.hideturtle()
        with open("data.txt") as data:
            self.highscore = int(data.read())

    def increment(self, score):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.highscore}", align="center", font=("Arial", 24, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0



   # def game_over(self):
   #     self.goto(0, 0)
   #     self.write(arg="GAME OVER", move=False, align="center", font=("Arial", 24, "normal"))