try:
    fromFile = input("Enter the Name of the file:")
    toFile = input("Enter the name of the NEW file:")
 
    fileR = open(fromFile,"r")
    data = fileR.read()
    fileW = open(toFile,"w")
    fileW.write(data)
 
 
except FileNotFoundError:
    print("File not Found")