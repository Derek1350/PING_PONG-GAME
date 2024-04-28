from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self,name1,name2):
        super().__init__()
        self.name1=name1
        self.name2=name2
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()
        

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 190)
        self.write(self.l_score, align="center", font=("Courier", 50, "normal"))
        self.goto(-100,245)
        self.write(self.name1, align="center", font=("Courier", 30, "normal"))
        self.goto(100, 190)
        self.write(self.r_score, align="center", font=("Courier", 50, "normal"))
        self.goto(100,245)
        self.write(self.name2, align="center", font=("Courier", 30, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()