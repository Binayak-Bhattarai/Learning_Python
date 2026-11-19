# a simple calcution for displaying electricity bill upto two decimal place



consumption = float(input("Enter number of units consumed: "))
per_unit = float(input("Enter cost per unit: "))

service_charge = 50

electricity_charge = consumption * per_unit
total = electricity_charge + service_charge

print("\n----- Electricity Bill -----")
print(f"Units consumed:       {consumption:.2f}")
print(f"Cost per unit:        Rs. {per_unit:.2f}")
print(f"Electricity charge:   Rs. {electricity_charge:.2f}")
print(f"Service charge:       Rs. {service_charge:.2f}")
print("---------------------------")
print(f"Total bill:           Rs. {total:.2f}")
