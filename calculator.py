def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    if n2 == 0:
        return "Error: Cannot divide by zero"
    return n1 / n2

calculatorDictionary = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

repeat = True
n1 = None

while repeat:
    if n1 is None:
        n1 = float(input("Type the first number: "))
    operator = input("What operation would you like to do? (+, -, *, /) ")
    n2 = float(input("Type the second number: "))

    result = calculatorDictionary[operator](n1, n2)
    print(f"{n1} {operator} {n2} = {result}")

    choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
    if choice == "y":
        n1 = result
    else:
        n1 = None
        print("\n" * 25)