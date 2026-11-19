#a program that accepts an integer and checks:
#1. Whether the number is even or odd.
#2. Whether it is divisible by 5.
#3. Whether it is divisible by both 3 and 5.

num= int(input("Enter a number to check\t"))

if (num%2==0):
    print(num,"is an even ineteger")
else:
    print(num,"is an odd interger")

if(num%5==0):
    print(num,"is divisible by 5")
if(num%5==0 and num%3==0):
    print(num,"is divisible by both 3 and 5")
