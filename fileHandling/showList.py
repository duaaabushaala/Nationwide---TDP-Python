read_file = open("studentList.txt", "r")
counter = 1
for line in read_file:
    print(str(counter), line)
    counter += 1

read_file.close()
