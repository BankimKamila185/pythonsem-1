import math

# Function to calculate area and perimeter of a circle
def circle(radius):
    area = math.pi * (radius ** 2)
    perimeter = 2 * math.pi * radius
    return area, perimeter


# Main program execution
def main():
    print("Welcome to the Area & Perimeter Calculator!")
    print("Choose a shape:")
