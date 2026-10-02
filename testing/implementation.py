def tax_calculator(salary):

    if salary < 1000:
        return 0

    elif salary <= 2000:
        return salary * 0.10

    else:
        return salary * 0.20