#Write a program that:
#1. Accepts a number from the user.
#2. Prints its multiplication table from 1 to 10.
#3. Asks the user whether they want another table.
#4. If the user enters yes, repeat the process.
#5. Otherwise, terminate the program.
repeat=True
while(repeat):
    num= int(input("Enter a number:\t"))

    if num<0:
        print("Enter a postitve number !!")
    else:
      print("Printing multiplication tabe of ",num,"\n") 
      for i in range(1,11):
         print(num,"x",i,"=",num*i,)
      print("Do you want to print another table??") 
      choice=input("(yes or no)")   
      if(choice.lower()=="yes"):
         repeat=True;
      else:
         repeat=False
         print("code executed successfully!")
     
