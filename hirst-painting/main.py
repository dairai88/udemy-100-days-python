"""Hirst Painting"""
import turtle
import random
import colorgram

colors = colorgram.extract('10hirst1-articleLarge.webp', 30)
color_rgbs = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

turtle.colormode(255)
tim = turtle.Turtle()
tim.setheading(225)
tim.hideturtle()
tim.penup()
tim.forward(300)
tim.setheading(0)
NUMBER_OF_DOTS = 100

for dot_count in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_rgbs))
        tim.penup()
        tim.forward(50)

    tim.setheading(90)
    tim.penup()
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)

SCREEN = turtle.Screen()
SCREEN.exitonclick()
