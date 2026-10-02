


def doSomething(a,b):

    result = a/b
    print("REsult:",result)




def Test1():
    doSomething(4/0)


def Test2():
    try:
        Test1()
    except ZeroDivisionError:
        print("Zero Division ----------1")

def Test3():
    Test2()


try:
    Test3()

except ZeroDivisionError:
    print("Zero Division")
