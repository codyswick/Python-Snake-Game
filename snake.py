# Snake Game By Cody Swick
# using turtle module
# made in november 2018


# 1. eat rabbits to grow
# 2. scorpions get rid of your body and costs 5 points you still maintain speed increse
# 3. hitting the wall will reset your score and speed
# 4. hitting your body will also reset your score and speed

#
# Import Modules
#

import turtle
import time
import random
import winsound
import tkinter
import os

#
# Set animation speed of snake using time module
#

delay = 0.1


#
# Set the Score and High Score Variables
#
#
score = 0
high_score = 0

#
# draw screen, set BG color, title, and size
#

wn = turtle.Screen()
wn.title("Snake Game by Cody Swick")
wn.bgcolor("yellow")
wn.bgpic("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\BG2.gif")
wn.setup(width=600, height=600)
wn.tracer(0)
winsound.PlaySound("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\snake_BG.wav", winsound.SND_ASYNC)





#
# register images to use as shapes
#


wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_up.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_down.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_left.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_right.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\body.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\rabbit.gif")
wn.register_shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\scorpion.gif")

#
# create the snake head
#

head = turtle.Turtle()
head.speed(0)
head.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_up.gif")
head.color("black")
head.penup()
head.goto(0,0)
head.direction = "stop"


#
# create the Food
#

food = turtle.Turtle()
food.speed(0)
food.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\rabbit.gif")
food.color("red")
food.penup()
food.goto(0,100)

#
# create the scorpion
#


food_bad = turtle.Turtle()
food_bad.speed(0)
food_bad.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\scorpion.gif")
food_bad.color("blue")
food_bad.penup()
food_bad.goto(0,-100)

#
# create an empty list called segments
#
segments = []

#
#draw pen
#

pen =turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Score:  0    High Score:  0", align=("center"), font=("Courier", 24, "normal"))

#
# deffine the directions
#

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

#
#Score functions
#


def write_score():
 pen.clear()
 pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))




#
# move functions
#

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
        head.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_up.gif")

    if head.direction == "down":
            y = head.ycor()
            head.sety(y - 20)
            head.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_down.gif")

    if head.direction == "left":
                x = head.xcor()
                head.setx(x - 20)
                head.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_left.gif")

    if head.direction == "right":
                    x = head.xcor()
                    head.setx(x + 20)
                    head.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\head_right.gif")

#
# get key press from user
#

wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_left,"a")
wn.onkeypress(go_right,"d")

while True:
    wn.update()

    # Check for a collision with the border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # Hide the segments
        for segment in segments:
            segment.goto(1000, 1000)

        # Clear the segments list
        segments.clear()

        # Reset the score
        score = 0

        # Reset the delay
        delay = 0.1

        write_score()

        # Check for a collision with the food
    if head.distance(food) < 40:
        # Move the food to a random spot
        x = random.randint(-260, 260)
        y = random.randint(-260, 260)
        food.goto(x, y)

        # Add a segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("D:\\Program Files\\PycharmProjects\\RandomNumberGame\\Snake\\body.gif")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # Shorten the delay
        delay -= 0.001

        # Increase the score
        score += 10

        if score > high_score:
            high_score = score

        write_score()

        # Check for a collision with the scorpion
    if head.distance(food_bad) < 40:
            # Move the scorpion to a random spot
         x = random.randint(-260, 260)
         y = random.randint(-260, 260)
         food_bad.goto(x, y)


         if score != 0:
             score -= 5
             for segment in segments:
                 segment.goto(1000, 1000)
             segments.clear()
            # Clear the segments list
             write_score()
         if score >= 0:
             head.direction = "stop"
             head.goto(0,0)
             for segment in segments:
                segment.goto(1000, 1000)
             write_score()


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

    # Check for head collision with the body segments
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # Hide the segments
            for segment in segments:
                segment.goto(1000, 1000)

            # Clear the segments list
            segments.clear()

            # Reset the score
            score = 0

            # Reset the delay
            delay = 0.1

            # Update the score display
            write_score()

    time.sleep(delay)

wn.mainloop()
