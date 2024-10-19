import math

def calculate_circle(radius):
    area = math.pi * radius ** 2
    perimeter = 2 * math.pi * radius
    return area, perimeter

def calculate_square(side):
    area = side ** 2
    perimeter = 4 * side
    return area, perimeter

def calculate_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter

def calculate_triangle(base, height, side1, side2):
    area = 0.5 * base * height
    perimeter = base + side1 + side2
    return area, perimeter

def main():
    while True:
        print("\nChoose a shape to calculate Area and Perimeter:")
        print("1. Circle")
        print("2. Square")
        print("3. Rectangle")
        print("4. Triangle")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            radius = float(input("Enter the radius of the Circle: "))
            area, perimeter = calculate_circle(radius)
            print(f"Circle - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

        elif choice == '2':
            side = float(input("Enter the side length of the Square: "))
            area, perimeter = calculate_square(side)
            print(f"Square - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

        elif choice == '3':
            length = float(input("Enter the length of the Rectangle: "))
            width = float(input("Enter the width of the Rectangle: "))
            area, perimeter = calculate_rectangle(length, width)
            print(f"Rectangle - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

        elif choice == '4':
            base = float(input("Enter the base of the Triangle: "))
            height = float(input("Enter the height of the Triangle: "))
            side1 = float(input("Enter the length of the first side of the Triangle: "))
            side2 = float(input("Enter the length of the second side of the Triangle: "))
            area, perimeter = calculate_triangle(base, height, side1, side2)
            print(f"Triangle - Area: {area:.2f}, Perimeter: {perimeter:.2f}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
