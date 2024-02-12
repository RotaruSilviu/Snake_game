from turtle import Turtle

### Cand ai setari ce se pot schimba din cod cel mai bine ar fi sa fie hard bodied la inceput in așa fel cand ai
# nevoie sa schimbi ceva la interfata se poate face usor din primele randuri.
ALINGMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALINGMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as data:
                data.write(str(self.score))
        self.score = 0
        self.update_scoreboard()

    # def game_over(self):
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALINGMENT, font=FONT)
