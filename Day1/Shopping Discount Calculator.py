# a simple calculator for calcutating discount

mp= float(input("Enter marked price of the product  "))
d= float(input("Enter dicount provided in percentage "))

price_afrer_discount= mp- ((d/100)*mp)
print("Price of product after",d,"% discount is",price_afrer_discount)