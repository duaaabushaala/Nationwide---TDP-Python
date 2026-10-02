file1 = open("studentList.txt", "a")
sno1 = 1
while True:
    name = input(str(sno)+ ". Enter Student's name:")
    sno+=1
    if name == "":
        break
    file1.write(name)
    file1.write("\n")

file1.close()