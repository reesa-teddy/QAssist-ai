passed = input("Passed tests: ")

try:
    passed_int = int(passed)
    print("Passed:", passed_int)
except ValueError:
    print("Invalid input:", passed)
    print("Please enter a whole number, e.g. 18")