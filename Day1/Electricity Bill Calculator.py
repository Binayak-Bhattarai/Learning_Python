# Build an electricity bill calculator using the following progressive tariff:

# Consumption          Rate
# First 20 units       Rs. 4/unit
# Next 30 units        Rs. 7/unit (21–50)
# Next 50 units        Rs. 10/unit (51–100)
# Above 100 units     rs.12/unit

consumption = float(input("Enter number of units consumed: "))


service_charge = 50
if(consumption<0):
    print("Plsease enter correct value")
else:
    if(consumption<=20):
     electricity_charge = consumption * 4   
     total = electricity_charge + service_charge
    elif(consumption>20 and consumption<=50 ):
     electricity_charge = (20*4)+(consumption-20)*7 
     total = electricity_charge + service_charge  
    elif(consumption>50 and consumption<=100 ):
     electricity_charge = (20*4)+(30*7)+(consumption-50)*10
     total = electricity_charge + service_charge
    else:   
        electricity_charge = (20*4)+(30*7)+(50*10)+(consumption-100)*12
        total = electricity_charge + service_charge
    print("\n----- Electricity Bill -----")
    print(f"Units consumed:       {consumption:.2f}")
    print(f"Electricity charge:   Rs. {electricity_charge:.2f}")
    print(f"Service charge:       Rs. {service_charge:.2f}")
    print("---------------------------")
    print(f"Total bill:           Rs. {total:.2f}")