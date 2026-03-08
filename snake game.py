# import required modules
import turtle
import time
import random

delay = 0.1
score = 0
high_score = 0


# Creating a window screen
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("green")
wn.setup(width=600, height=600)
wn.tracer(0)

# head of the snake
head = turtle.Turtle()
head.shape("square")
head.color("black")
head.penup()
head.goto(0, 0)
head.direction = "Stop"

# food in the game
food = turtle.Turtle()
food.speed(0)
food.shape(random.choice(['triangle', 'circle']))
food.color(random.choice(['red', 'brown', 'yellow']))
food.penup()
food.goto(0, 100)

# score display
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 250)
pen.write(
    "Score : 0                                   High Score : 0",
    align="center",
    font=("candara", 24, "bold")
)

segments = []


# assigning key directions
def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        head.sety(head.ycor() + 20)

    elif head.direction == "down":
        head.sety(head.ycor() - 20)

    elif head.direction == "left":
        head.setx(head.xcor() - 20)

    elif head.direction == "right":
        head.setx(head.xcor() + 20)


def reset_game():
    global score, delay

    time.sleep(1)
    head.goto(0, 0)
    head.direction = "Stop"

    for segment in segments:
        segment.goto(1000, 1000)

    segments.clear()
    score = 0
    delay = 0.1

    pen.clear()
    pen.write(
        "Score : {}                                   High Score : {}".format(score, high_score),
        align="center",
        font=("candara", 24, "bold")
    )


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")


# Main Gameplay
try:
    while True:
        wn.update()

        # Check for collision with border
        if (
            head.xcor() > 290 or head.xcor() < -290 or
            head.ycor() > 290 or head.ycor() < -290
        ):
            reset_game()

        # Check for collision with food
        if head.distance(food) < 20:
            x = random.randint(-270, 270)
            y = random.randint(-270, 270)
            food.goto(x, y)

            food.shape(random.choice(['triangle', 'circle']))
            food.color(random.choice(['red', 'brown', 'yellow']))

            # Adding segment
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("orange")
            new_segment.penup()
            segments.append(new_segment)

            delay = max(0.05, delay - 0.001)
            score += 10

            if score > high_score:
                high_score = score

            pen.clear()
            pen.write(
                "Score : {}                                   High Score : {}".format(score, high_score),
                align="center",
                font=("candara", 24, "bold")
            )

        # Move the end segments first in reverse order
        for index in range(len(segments) - 1, 0, -1):
            x = segments[index - 1].xcor()
            y = segments[index - 1].ycor()
            segments[index].goto(x, y)

        # Move segment 0 to where the head is
        if len(segments) > 0:
            x = head.xcor()
            y = head.ycor()
            segments[0].goto(x, y)

        move()

        # Check for head collision with body
        for segment in segments:
            if segment.distance(head) < 20:
                reset_game()
                break

        time.sleep(delay)

except turtle.Terminator:
    pass
