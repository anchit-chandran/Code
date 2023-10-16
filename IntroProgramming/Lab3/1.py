"""1. Write a function that calculates the surface area of a cylinder based on the radius
and height entered as command line arguments."""

import math


def get_surface_area_cylinder(radius, height):
    return 2 * math.pi * radius * height + 2 * math.pi * radius**2


def solution_1():
    radius = float(input("Please enter radius: "))
    height = float(input("Please enter height: "))
    
    return get_surface_area_cylinder(radius=radius, height=height)

print(solution_1())
