values = __import__("random").choices(range(1, 7), k=3)
print(f"The values on the dice are {', '.join(map(str, values))}, and their sum is {sum(values)}")
