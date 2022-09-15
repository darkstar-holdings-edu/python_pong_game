from turtle import Turtle


class ScoreBoard(Turtle):

    left_score: int = 0
    right_score: int = 0

    def __init__(self):
        super().__init__()

        self.color("white")
        self.penup()
        self.hideturtle()

        self.update_score()

    def point_left(self):
        self.left_score += 1
        self.update_score()

    def point_right(self):
        self.right_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.setposition(x=-100, y=200)
        self.write(self.left_score, align="center", font=("Courier", 80, "normal"))
        self.setposition(x=100, y=200)
        self.write(self.right_score, align="center", font=("Courier", 80, "normal"))
