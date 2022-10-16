#1 Write a function called calculate_area that takes base and height as an input and returns and area of a triangle.

def calculate_area(base, height):
    area = (1/2) * base * height
    return area

area = calculate_area(5, 7)
print(area)

#2 Modify above function to take third parameter shape type. It can be either "triangle" or "rectangle". Based on shape type it will calculate area.


def calculate_area(a, b, shape="triangle"):
    if shape == "rectangle":
        area = a * b
        return area
    else:
        area = (1/2)*a*b
        return area

area = calculate_area(5, 6)
print(area)

# 3. Write a function called print_pattern that takes integer number as an argument and prints following pattern if input number is 3,
# ```
# *
# **
# ***
# ```
# if input is 4 then it should print
# ```
# *
# **
# ***
# ****
# ```
# Basically number of lines it prints is equal to that number. (Hint: you need to use two for loops)

def print_pattern(n=5):
    for i in range(n):
        s = " "
        for j in range(i+1):
            s += "*"
        print(s)

print(print_pattern(3))
