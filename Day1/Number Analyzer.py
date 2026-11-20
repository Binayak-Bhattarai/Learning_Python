# a simple program to check if a user given integer is positive negative or zero

num= int(input("Enter a number to check\t"))

if num<0:
    print(num,"is a negative ineteger")
elif num >0:
    print(num,"is a positive interger")
else:
    print("Its zero!!")    