import math

def sphere_area(radius):
    return 4 * math.pi * radius ** 2

def sphere_volume(radius):
    return (4/3) * math.pi * radius ** 3

def cube_area(side):
    return 6 * (side ** 2)

def cube_volume(side):
    return side ** 3

def cuboid_area(length, width, height):
    return 2 * (length * width + width * height + height * length)

def cuboid_volume(length, width, height):
    return length * width * height

def cone_area(radius, height):
    slant_height = math.sqrt(radius ** 2 + height ** 2)
    return math.pi * radius * (radius + slant_height)

def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

def main():
    print("Choose a shape to calculate area and volume:")
    print("1. Sphere")
    print("2. Cube")
    print("3. Cuboid")
    print("4. Cone")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        radius = float(input("Enter the radius of the sphere: "))
        print(f"Area of Sphere: {sphere_area(radius)}")
        print(f"Volume of Sphere: {sphere_volume(radius)}")
        
    elif choice == '2':
        side = float(input("Enter the side length of the cube: "))
        print(f"Area of Cube: {cube_area(side)}")
        print(f"Volume of Cube: {cube_volume(side)}")
        
    elif choice == '3':
        length = float(input("Enter the length of the cuboid: "))
        width = float(input("Enter the width of the cuboid: "))
        height = float(input("Enter the height of the cuboid: "))
        print(f"Area of Cuboid: {cuboid_area(length, width, height)}")
        print(f"Volume of Cuboid: {cuboid_volume(length, width, height)}")
        
    elif choice == '4':
        radius = float(input("Enter the radius of the cone: "))
        height = float(input("Enter the height of the cone: "))
        print(f"Area of Cone: {cone_area(radius, height)}")
        print(f"Volume of Cone: {cone_volume(radius, height)}")

    elif choice == '5':
         print("Exiting the program.")
         
        
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()

