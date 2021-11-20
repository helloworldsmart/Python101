import turtle
from turtle import Turtle, Screen
import random
# import turtle as t
# import heroes
# print(heroes.gen())


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("red")
# timmy_the_turtle.forward(100)
# timmy_the_turtle.right(90)

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.left(90)

# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

tim = Turtle()
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

# My answer
# for i in range(3, 9):
#     r = 360 / i
#     for _ in range(i):
#         tim.forward(100)
#         tim.right(r)

#colours = ["dark slate gray", "royal blue", "firebrick", "medium spring green", "dark magenta", "yellow", "sky blue", "deep pink"]


directions = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range(200):
    # tim.color(random.choice(colours))
    tim.color(random_color())
    tim.forward(20)
    tim.setheading(random.choice(directions))

# My answer

# angles = [90, 180, 270, 360]
# for _ in range(50):
#     tim.color(random.choice(colours))
#     tim.right(random.choice(angles))
#     tim.forward(10)

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
#
# for shape_side_n in range(3, 11):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

screen = Screen()
screen.exitonclick()

