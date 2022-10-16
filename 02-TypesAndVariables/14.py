celsius = float(input("Enter Temperature in °C:\n> "))
fahrenheit = celsius * 1.8 + 32
kelvin = celsius + 273.15

print(f"\n|{'Scale':^15}|{'Temperature':^15}|")
print("-" * 33)
print(f"|{'Celsius':^15}|{f'{celsius:.2f}°':^15}|")
print(f"|{'Fahrenheit':^15}|{f'{fahrenheit:.2f}°':^15}|")
print(f"|{'Kelvin':^15}|{kelvin:^15}|")
