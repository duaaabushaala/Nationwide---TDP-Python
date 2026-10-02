listOfWords=[]
def checkUnique(word):
 
    for wrd in listOfWords:
        if wrd==word:
           
            return False
    listOfWords.append(word)
    return True
 
 
file1 = open("data.txt","r")
msg = file1.read()
 
 
msg2=""
i=0
word=""
while i<len(msg):
 
    if msg[i]==" ":
        if checkUnique(word):
            msg2 += " " + word
        word=""
    else:
        word+=msg[i]
 
    i+=1
 
print(msg2)
 
 
 