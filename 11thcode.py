a=int(input("Enter the number: "))
num=a
rev=0
while a>0:
    b=a%10
    a=a//10
    rev=(rev*10)+b
print(rev)   
if rev==num:
    print("Palindrome")
else:
    print("Not a palindrome")