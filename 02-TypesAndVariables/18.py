a, b, c = (float(x) for x in input("Enter the sides of the triangle, separated with spaces:\n> ").split(" "))
s = (a + b + c) / 2
area = (s * (s - a) * (s - b) * (s - c))**(1 / 2)

print(f"The triangle's area is {area}")
