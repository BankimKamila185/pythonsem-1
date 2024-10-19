import math

# Function to calculate area and perimeter of a circle
def circle(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter

# Function to calculate area and perimeter of a square
def square(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

# Function to calculate area and perimeter of a rectangle
def rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

# Function to calculate area and perimeter of a triangle
def triangle(base, height, side1, side2):
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    return area, perimeter

# Main program execution
def main():
    print("Welcome to the Area & Perimeter Calculator!")
    print("Choose a shape:")
