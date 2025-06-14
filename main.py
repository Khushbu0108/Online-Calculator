import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return  n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("pick the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("pick an operation: ")
        num2= float(input("pick the second number?: "))
        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'yes' to continue calculation with the {answer}, or 'no' to start the new calculation: ").lower()

        if choice == "yes":
            num1 = answer
        else:
            should_accumulate =  False
            print("\n" * 20)
            calculator()

calculator()
