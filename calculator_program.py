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
num1 = int(input("What's the first number? "))
num2 = int(input("What's the secund number? "))

for n in operations:
    print(n)
choosen = input("Which operations will you use?")
"""
answer = 0
if choosen == "+":
    answer = add(num1, num2)
elif choosen == "-":
    answer = subtract(num1, num2)
elif choosen == "*":
    answer = multiply(num1, num2)
elif choosen == "/":
    answer = divide(num1, num2)
"""
calculation_function = operations[choosen]
answer = calculation_function(num1, num2)
print(f"{num1} {choosen} {num2} = {answer}")
