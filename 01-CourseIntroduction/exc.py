# 2.15

def exc2():
    name = input("Enter your name: ")
    print(f"Hello, {name}")


def exc3():
    hours = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    print(f"Pay: {round(hours*rate, 2)}")


def exc5():
    celsius = float(input("Enter Temp in °C: "))
    print(f"Temp in °F: {round(celsius * 1.8 + 32, 5)}")


table = {2: exc2, 3: exc3, 5: exc5}
