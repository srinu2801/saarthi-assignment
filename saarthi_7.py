in_pass = input("Enter your password : ")

length = len(in_pass)

specialChar = ["!","\"","#","$","%","&","'","(",")","*","+",",","-",".","/",":",";","<","=",">","?","@","[","\\","]","^","_","`","{","|","}","~"]

l=0
u=0
n=0
sp=0

for i in in_pass:
    if i.islower():
        l+=1
    if i.isupper():
        u+=1
    if i.isdigit():
        n+=1
    if i in specialChar:
        sp+=1

if (length>=6 and length<=16 and l>=1 and u>=1 and n>=1 and sp>=1 and l+u+n+sp == length):
    print("Valid Password")
else:
    print("Invalid Password")


