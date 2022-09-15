from turtle import Turtle


class Ball(Turtle):

    x_move: int = 10
    y_move: int = 10
    move_speed: float = 0.1

    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.penup()

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def move(self):
        x_cor = self.xcor() + self.x_move
        y_cor = self.ycor() + self.y_move
        self.setposition(x=x_cor, y=y_cor)

    def reset(self):
        self.home()
        self.bounce_x()
        self.move_speed = 0.1
