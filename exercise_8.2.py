"""
Write circle_calc() function that takes radius of a circle as an input from user and then it calculates and returns area, circumference and diameter. You should get these values in your main program by calling circle_calc function and then print them
"""
import math

def circle_calc(r):
    area = math.pi * (r**2)
    area = round(area, 2)
    circumference = 2 * math.pi * r
    circumference = round(circumference, 2)
    d = r * 2
    d = round(d, 2)
    print(f"Area of the circle is {area}, circumference is {circumference} and diameter is {d}.")
    return area, circumference, d

circle_calc(5)