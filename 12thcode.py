print("Palindrome or not")
s=input("Enter the string: ")
reverse=s[::-1]
print("Reversed string is:",reverse)
if s==reverse:
    print("Palindrome")
else:
    print("Not a palindrome")