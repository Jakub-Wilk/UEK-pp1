(x:=int(input("Enter number: ")),y:=1,z:=lambda x,y:((print(f"{x} x {y} = {x*y}"),y:=y+1,z(x,y)) if y<=10 else ()),z(x,y))