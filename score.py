from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.sco_1=0
        self.sco_2=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,360)
        

    def score_pord(self):
        self.write(f"Score: {self.sco_1}   Score: {self.sco_2 } ", align="center",font=("Arial",24,"normal"))

    def game_over(self):
        self.color("red")
        self.hideturtle()
        self.penup()
        self.goto(0,0)
        self.write(f"game over ", align="center",font=("Arial",40,"normal"))

    def updat_1(self):
        self.sco_1 +=1
        self.clear()
        self.score_pord()

    def updat_2(self):
        self.sco_2 +=1
        self.clear()
        self.score_pord()
        