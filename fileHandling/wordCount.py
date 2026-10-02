file1=open("data.txt","r")
 
msg = file1.read()
 
 
count = 1
 
i = 0
 
while i<len(msg):
    if msg[i]== " ":
        count+=1
    i+=1
print(count ," words you have entered")
 