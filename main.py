from turtle import Screen
from game import Paddle, Ball, ScoreBoard
import time


def main():
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("Pong!")
    screen.tracer(0)
    screen.listen()

    right_paddle = Paddle(position=(350, 0))
    screen.onkeypress(key="Up", fun=right_paddle.move_up)
    screen.onkeypress(key="Down", fun=right_paddle.move_down)

    left_paddle = Paddle(position=(-350, 0))
    screen.onkeypress(key="a", fun=left_paddle.move_up)
    screen.onkeypress(key="z", fun=left_paddle.move_down)

    ball = Ball()
    score_board = ScoreBoard()

    game_running = True
    while game_running:
        ball.move()
        # score_board.update_score()
        screen.update()

        if ball.ycor() > 280 or ball.ycor() < -275:
            ball.bounce_y()

        elif (
            ball.xcor() > 320
            and ball.distance(right_paddle) < 50
            or ball.xcor() < -320
            and ball.distance(left_paddle) < 50
        ):
            ball.bounce_x()

        elif ball.xcor() > 375:
            score_board.point_left()
            ball.reset()

        elif ball.xcor() < -375:
            score_board.point_right()
            ball.reset()

        time.sleep(ball.move_speed)

    screen.exitonclick()


if __name__ == "__main__":
    main()
