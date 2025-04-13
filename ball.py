from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.goto(0,0)
        self.me_y=10
        self.me_x=7
        
        

    def again(self):
        self.goto(0,0)
        self.me_x *=-1
        self.me_y *=-1
        self.move()


    def move(self):
        self.clear()
        n_y=self.ycor()+self.me_y
        n_x=self.xcor()+self.me_x
        self.goto(n_x,n_y)
