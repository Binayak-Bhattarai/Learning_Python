#Accept an integer from the user.
#Check whether it is divisible by any number other than 1 and itself.
#Display whether the number is prime or composite.
#Handle numbers less than 2 separately.

num= int(input("Enter a number:\t"))
count=0

if num<0:
     print("Enter a postitve number !!")
elif(num==0 or num==1):
     print(num,"is neither prime nor composite")
else:
    for i in range(2,num):
       if(num%i==0):
         count+=1
         break;
    if(count==0):
     print(num,"is a prime number")
    else:
     print(num,"is a composite number")

  