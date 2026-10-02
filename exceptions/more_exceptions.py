try:
    numbers=[4,3,4] # example

    print(numbers[4])
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))


    result = num1/num2
    print("First number: ", num1)
    print("Second numner: ", num2)
    print("- - - - - - - - - - - - - - - - - ")
    print("The result is ", result)



except ZeroDivisionError:
    print("You cannot divide anything by zero")
except ValueError:
    print("Only numbers please!")
except IndexError:
    print("The index which you are looking for does not exist")
print("Program finished!")