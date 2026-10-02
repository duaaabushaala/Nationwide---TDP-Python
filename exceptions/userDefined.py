class AbsentiesException(Exception):
    pass

def payslip(name, sal, absenties):
    if absenties >= 5:
        ref = AbsentiesException()
        raise ref

    tax = sal*21/100
    print("Name of employee: ", name)
    print("Salary:", sal)
    print("Tax", tax)
    print("Net Salary: ", (sal-tax))


try:
    payslip("shafeeq", 4000, 10)
except AbsentiesException:
    print("Thats fine he is shafeeq")


try:
    payslip("shafeeq", 4000, 10)
except AbsentiesException:
    print("Not allowed please see your manager")

