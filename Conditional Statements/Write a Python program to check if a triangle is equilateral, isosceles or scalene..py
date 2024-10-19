def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral triangle"
    elif a == b or b == c or c == a:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"

a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
c = float(input("Enter the length of side c: "))

if a + b > c and b + c > a and c + a > b:
    print(triangle_type(a, b, c))
else:
    print("The given sides do not form a valid triangle")

