# Calculator


# Add
def add(n1, n2):
    return n1 + n2
# Subtract


def subtract(n1, n2):
    return n1 - n2

# Multoply


def multiply(n1, n2):
    return n1 * n2

# Divide


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,

}


def calculation():
    num1 = float(input("What's the first number? "))
    for n in operations:
        print(n)
    should_continue = True
    while should_continue:

        choosen = input("Pick an operation :")
        num2 = float(input("What's the secund number? "))
        calculation_function = operations[choosen]
        answer = calculation_function(num1, num2)

        print(f"{num1} {choosen} {num2} = {answer}")

        if input(f"Type 'y' to continue calclate with {answer}, or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False
            calculation()


calculation()
