# while True: __import__("random").seed(__import__("os").getpid()), __import__("sys").exit("True") if int(input("Enter a number:\n> ")) == __import__("random").randint(1, 6) else print("Wrong, try again")
(x:=__import__("random").randint(1,6),y:=lambda:(__import__("sys").exit("True") if x==int(input("Enter your guess:\n> ")) else print("False"),y()),y())
# One line, without semicolons :)
