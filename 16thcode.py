a=int(input("Enter the number:"))
n=len(str(a))
dig=0
b=a
while(a>0):
    c=a%10
    a=a//10
    dig=dig+c**n
print(dig)
if(dig==b):
    print("Armstrong")
else:
    print("Not Armstrong")
