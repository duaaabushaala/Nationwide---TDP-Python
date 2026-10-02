

try:

    # connected to US servers
    # connected to London servers

    numbers=[4,3,4]

    print( numbers[0])
    num1 = int(input("Enter First Number:"))
    num2 = int(input("Enter Second Number:"))

    result = num1/num2
    print("First Number:",num1)
    print("Second Number:",num2)
    print("--------------------------------")
    print("The Result is:",result)

except ZeroDivisionError:
    print("You can't divide anything by ZERO")
except ValueError:
    print("Exceue me....... only numbers please")
except IndexError:
    print("The Index which you are lookign for , does not exist")
except:
    print("--- Something went Wrong----")




print("Program finished")