print("Factorial of a number")
a=int(input("Enter the number: "))
sum=0
fact=1
while a>0:
    fact=fact*a
    a=a-1
print(fact)