f = lambda x,y: sum([int(z) for z in str(x) if int(z)%2]) if not y else sum([int(z) for z in str(x) if not int(z)%2])