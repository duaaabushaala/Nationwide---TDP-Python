class Results:

    def __init__(self):
        self.name=""
        self.__invalid=False # add a flag 
        self.__physics=0
        self.__maths=0

    def physicsMarks(self,phy):

        if phy>=0 and phy<=150:
            self.__physics=phy
        else:
            self.__invalid=True
            print("Invalid Physics Marks")

    def mathsMarks(self,mat):

        if mat>=0 and mat<=150:
            self.__maths=mat
        else:
            self.__invalid=True
            print("Invalid MATHS Marks")

    def printResults(self):

        if self.__invalid:
            print("You have Entered Invalid values")
        else:
            total = self.__physics + self.__maths
            per = total*100/300

            print("Name of the Student:",self.name)
            print("Total Marks:",total)
            print("Percentage:",per)
            print("-------------------------------------------")
            if per>=60:
                print("You have PASSED the exam")
            else:
                print("You have FAILED the Exam")

shafeeq=Results()
shafeeq.name="SHAFEEQ"
shafeeq.physicsMarks(97)
shafeeq.mathsMarks(89)
shafeeq.printResults()
