(x:=[],y:=lambda x:(z:=int(input("Enter number: ")),x.append(z) if z else (),y(x) if z else ()),y(x),print(f"RESULT: Quantity={len(x)}, Sum={sum(x)}, Mean={sum(x)/len(x)}"))