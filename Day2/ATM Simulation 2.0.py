# simple atm simulation 

balance =25000
pin=1234
chances=3
choice = 0
while(chances!=0):
    upin=int(input("Enter pin number:- \t"))
    if upin != pin:
        chances-=1
        if(chances==0):
            print("U entered wrng pin 3 time , program terminated!!")
            break
        else:
            print("Wrong PIN! You have", chances, "more chances.")
    else:
        print("pin is valid\n")
        chances=0
        while choice != 4:
            print("Enter 1 for checking balance")
            print("Enter 2 to deposit balance")
            print("Enter 3 to withdraw balance")
            print("Enter 4 to exit\n")

            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    print("Your current Balance is Rs", balance)

                case 2:
                    amount = float(input("Enter deposit amount: "))

                    if amount <= 0:
                        print("Invalid amount. Please enter a positive value.")
                    else:
                        balance += amount
                        print("Rs", amount, "was deposited successfully")
                        print("Your new balance is Rs", balance)

                case 3:
                    amount = float(input("Enter withdrawal amount: "))

                    if amount <= 0 or amount > balance:
                        print("Invalid amount. Please enter a valid amount.")
                    else:
                        balance -= amount
                        print("Rs", amount, "was withdrawn successfully")
                        print("Your new balance is Rs", balance)

                case 4:
                    print("Program exited successfully!")

                case _:
                    print("You made a wrong choice!")

            if choice != 4:
                answer = input("\nDo you want to continue? (yes/no): ").lower().strip()

                if answer == "no":
                    print("Thank you for using our ATM!")
                    break