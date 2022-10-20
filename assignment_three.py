# Sofia Fall
# 10/19/22
# This program prompts the user to enter a center color, a petal color, and the size of a side to generate
# a visual representation of a flower.

import unittest
import turtle


t = turtle.Turtle()
t.speed(15)


def get_side_length():
    """The function get_side_length() accepts no parameters and returns a float."""
    return float(input("Enter the length of a side, please. "))


def get_center_color():
    """The function get_center_color() accepts no parameters and returns a string."""
    return str(input("Enter the fill color of the flower's center:  "))


def get_petal_color():
    """The function get_petal_color() accepts no parameters and returns a string"""
    return str(input("Enter the fill color of the petals: "))


def draw_hexagon(size, color):
    """The function draw_hexagon accepts size (float) and color (string)
    as parameters and doesn't return anything"""
    t.begin_fill()
    t.fillcolor(color)
    for x in range(6):
        t.forward(size)
        t.left(300)
    t.end_fill()


def draw_flower(size, center, petal):
    """The function draw_flower draws the flower."""

    draw_hexagon(size, center)

    # move the pen to the right
    t.forward(size)
    t.left(180)

    for x in range(6):
        draw_hexagon(size, petal)
        t.forward(size)
        t.left(60)


def main():
    """The main() function that calls all the other functions."""
    # Prompt user to enter a side length
    length = get_side_length()

    # Prompt user to enter a color for the center of the flower
    center = get_center_color()

    # This statement assignment asks the user for the flowers petal color
    petal = get_petal_color()

    draw_flower(length, center, petal)


main()
