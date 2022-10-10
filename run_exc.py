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
            try:
                chapters = list(exc.table.keys())
                chapter = input((f"Choose chapter: {chapters}\n> "))
                if chapter == "stop":
                    break
                else:
                    chapter = int(chapter)
                if chapter not in exc.table.keys():
                    raise ValueError
            except ValueError:
                print("Invalid chapter")
                continue
            try:
                exercises = list(exc.table[chapter].keys())
                exercise = input(f"Choose exercise to run: {exercises}\n> ")
                if exercise == "stop":
                    break
                else:
                    exc.table[chapter][int(exercise)]()
            except ValueError:
                print("Invalid exercise number")
                continue
    except ImportError:
        print(f"No exercises found in module {module}")
        continue
