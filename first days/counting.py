alpha = [0] * 42
message = input("Enter any message")

for ch in message:
    alpha[ord(ch)-65] += 1

i = 0
while i <= 50:
    if alpha[i] > 0:
        print( chr(i+65), "->", alpha[i])
    i+=1 
                