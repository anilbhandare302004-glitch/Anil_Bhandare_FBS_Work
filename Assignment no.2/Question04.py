#WAP to calculate area of triangle and rectangle
#Triangle Area
b = float(input("Enter base of triangle: "))
h = float(input("Enter height of triangle: "))
triangle_area = 0.5 * b * h

# Rectangle Area
l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
rectangle_area = l * w

print("Area of Triangle =", triangle_area)
print("Area of Rectangle =", rectangle_area)