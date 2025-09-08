x=int(input("enter first number x: "))
y=int(input("enter second number y: "))
print("before swapping values of x and y are:",x,",",y)
x=x+y
y=x-y
x=x-y
print("after swapping values of x and y are:",x,",",y)