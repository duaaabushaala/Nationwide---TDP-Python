print("Program started")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    result = num1/num2

    print("First number: ", num1)
    print("Second number: ", num2)
    print("- - - - - - - - - - -")
    print("The result is: ", result)

except ZeroDivisionError:
    print("You can't divide anything by ZERO")

print("Program finished.")