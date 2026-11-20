#Write a program that:
#1. Accepts an integer n from the user.
#2. Prints all numbers from 1 to n.
#3. Prints whether each number is even or odd.
#4. Calculates the sum of all numbers from 1 to n.

num= int(input("Enter a number:\t"))

if num<0:
    print("Enter a postitve number !!")
else:
    sum=num*(num+1)//2;
    print("Printing numbers from 1 to ",num,"\n")
    for i in range(1,num+1):
     if(i%2==0):
        print(i,"is even\n")
     else:
        print(i,"is odd\n")
    print("sum of numbers:-\t",sum)   