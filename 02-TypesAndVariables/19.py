weight = int(input("Enter your weight in kg:\n> "))
height = int(input("Enter your height in cm:\n> "))

bmi = weight / (height / 100)**2

print(f"Your BMI index is {bmi:.2f}")
