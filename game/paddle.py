from turtle import Turtle


class Paddle(Turtle):
    move_speed: int = 20

    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__()

        self.color("white"),
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(position)

    def move_up(self):
        if self.ycor() < 230:
            self.sety(self.ycor() + self.move_speed)

    def move_down(self):
        if self.ycor() > -225:
            self.sety(self.ycor() - self.move_speed)
