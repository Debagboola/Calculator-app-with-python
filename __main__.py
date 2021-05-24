from calculator import SimpleCalculator

print("CALCULATOR")
print("----------")

calc = SimpleCalculator()
operations = calc.OPERATIONS
is_on = True

value1 = float(input("Input the first number: "))

while is_on:
    if value1 == int or float:
        for symbol in operations:
            print(symbol)
        operation = input("Pick an operation: ")
    else:
        value1 = float(input("Value not accepted. Input an integer or a float: "))

    if operation == "**":
        value2 = 0
    else:
        value2 = float(input("What's the second number?: "))
    result = calc.calculate(value1, value2, operation)
    print(result)
    keep_calculating = input(f"Continue calculating with {result}? Type 'y' or 'n': ")
    if keep_calculating == "y":
        value1 = result
    elif keep_calculating == "n":
        print("Thanks for using this calculator!")
        is_on = False
    else:
        keep_calculating = input(f"Type either 'y' or 'n' : ")

    # if operator == "-" or "*" or "/" or "+":
    #     value2 = input("Input the second number: ")
    # else:
    #     operator = input("Operator not accepted. Input - or + or * or /: ")




# def first_result():
#     if operator == "-":
#         calc.minus(value1, value2)
#
#     if operator == "*":
#         calc.multiply(value1, value2)
#
#     if operator == "/":
#         calc.divide(value1, value2)
#
#     if operator == "+":
#         calc.sum(value1, value2)


calculator = SimpleCalculator()
operations = calculator.OPERATIONS
is_on = True

operand_one = int(input("What's the first number?: "))
while is_on:
    for symbol in operations:
        print(symbol)
    operation = input(f"Pick an operation: ")
    if operation == "**":
        operand_two = 0
    else:
        operand_two = int(input("What's the second number?: "))
    answer = calculator.calculate(operand_one, operand_two, operation)
    print(answer)
    keep_calculating = input(f"Continue calculating with {answer}? Type 'y' or 'n': ")
    if keep_calculating == "y":
        if answer == None:
            operand_one = 0
        else:
            operand_one = answer
    else:
        is_on = False

