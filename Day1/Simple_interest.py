# a simple calculator to calculate simple interest for user provide principle , rate and interest

principal= float(input("Enter principle amount:\t"))
rate= float(input("Enter rate of interest:\t"))
time= float(input("Enter time in years:\t"))

SI=(principal*rate*time)/100

print("The simple interest for Rs",principal,"at rate of",rate,"% over time of",time,"years is",SI)

amount =principal+SI

print("The amount in your acount after",time,"years is",amount)