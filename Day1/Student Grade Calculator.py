# simple program to calculate grade of student

marks=int(input("enter your obtained marks "))

if( marks<50):
    print("Grade :F \n Result:Fail")
elif(marks>=90 and marks<=100):
    print("Grade :A \n Result:Pass")    
elif(marks>=80 and marks<90):
    print("Grade :B \n Result:Pass") 
elif(marks>=70 and marks<89):
    print("Grade :C \n Result:Pass")
elif(marks>=60 and marks<79):
    print("Grade :D \n Result:Pass")
else:
    print("Grade :E \n Result:Pass")   

