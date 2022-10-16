#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
radius = int(input("Enter the radius:\n> "))
pi = __import__("math").pi

# calculate area
area = pi * radius**2

# calculate circumference
circumference = 2 * pi * radius

# display results
print(f"\n|{'Property':^15}|{'Value':^15}|")
print("-" * 33)
print(f"|{'Radius':^15}|{radius:^15.2f}|")
print(f"|{'Area':^15}|{area:^15.2f}|")
print(f"|{'Circumference':^15}|{circumference:^15.2f}|")
