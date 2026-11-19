# simple atm simulation 

balance =25000
pin=1234


upin=int(input("Enter pin number:- \t"))

if upin != pin:
    print("You entered wrong pin\n program terminated...")
    
          
else:
    print("\n")
    print("pin is valid\n")
    print("Enter 1 for checking balance")
    print("Enter 2 to deposite balance")
    print("Enter 3 to withdraw balance")
    print("Enter 4 for exiting\n ")
    choice=int(input(" Enter your choice :\t"))
    match choice:
        case 1:
            print("Your current Balance is ",balance)
        case 2:
            amount=float(input("enter deposite amount\t"))
            if(amount<=0 ):
                print("You entered wrong amount , program terminated!!")
            else:
                balance= balance + amount
                print("Rs",amount,"was deposited successfully")
                print("your new balance is Rs",balance)
                print("Program executed successfully\n")
        case 3:
            amount=float(input("enter withdraw amount\t"))
            if(amount<=0 or amount >balance):
                print("You entered wrong amount , program terminated!!")
            else:
                 balance= balance - amount
                 print("Rs",amount,"was withdrawn successfully")
                 print("your new balance is Rs",balance)
                 print("Program executed successfully\n")
        case 4:
            print("Program exited successfully\n")  
        case _:
            print("You made wrong choice, program terminated!!\n")   