class Forth:

    def __init__(self):
        self.__salary=1000

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 1000:
            print("Invalid Salary")
        else:
            self.__salary = value

ref=Forth()
print(ref.salary)

ref.salary=50
print(ref.salary)
