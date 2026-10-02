listOfWords = []
def checkUnique(word):

    for wrd in listOfWords:
        if wrd == word:
            return False

    listOfWords.append(word)
    return True

msg=input("Enter any message: ")
msg2= ""
i = 0
word = ""
while i < len(msg):
    if msg[i] == "":
        if checkUnique(word):
            msg2 += " " + word
        word = ""
    else:
        word+msg[i]

    i+=1