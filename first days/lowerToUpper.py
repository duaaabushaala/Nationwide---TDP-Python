 
message = input("Enter a message: ")
newMsg=""

for ch in message:
    if ord(ch) >= 65 and ord(ch)<=90:
        newMsg += chr(ord(ch) + 32) # capital letter
    elif ord(ch) >= 90 and ord(ch) <= 122:
        newMsg += chr(ord(ch) - 32) # lowercase letter
    elif ord(ch) >= 48 and ord(ch) <= 57:
        newMsg += str(int(ch)*2)
    else:
        newMsg += ch
print(newMsg)