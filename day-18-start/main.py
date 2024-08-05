"""Turtle Demo"""
import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

directions = [0, 90, 180, 270]


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def random_walk():
    """turtle random walk"""
    tim.width(10)
    tim.speed("fastest")
    for _ in range(200):
        tim.color(random_color())
        tim.forward(30)
        tim.setheading(random.choice(directions))
        tim.heading()


random_walk()

SCREEN = turtle.Screen()
SCREEN.exitonclick()
