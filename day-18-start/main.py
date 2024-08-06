"""Turtle Demo"""
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def draw_spirograph(gap_size):
    for _ in range(int(360 / gap_size)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + gap_size)


draw_spirograph(5)

SCREEN = turtle.Screen()
SCREEN.exitonclick()
