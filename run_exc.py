from pathlib import Path
from importlib import import_module
here = Path(".")
course_modules = {int(x.stem[:2]): x.stem for x in here.iterdir() if x.is_dir() and x.stem[0].isnumeric()}

while True:
    try:
        module = int(input("Which module would you like to check the exercises for?\n> "))
        if module not in range(1, 16):
            raise ValueError
    except ValueError:
        print("Modules must be integers 1-15")
    try:
        exc = import_module(f"{course_modules[module]}.exc")
        print(f"Running exercises from module {module}. To stop, type 'stop'.")
        while True:
            exercises = list(exc.table.keys())
            print("Choose exercise to run: ", exercises)
            action = input("> ")
            if action == "stop":
                break
            else:
                try:
                    exc.table[int(action)]()
                except ValueError:
                    print("Invalid exercise number")
    except ImportError:
        print(f"No exercises found in module {module}")
        continue