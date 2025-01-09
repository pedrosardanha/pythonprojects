income = float(input("Entre com os rendimentos: "))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 + (income - 85528) * 0.32

if tax < 0:
    tax = 0

tax = round(tax)

print("A taxa é:", tax, "thalers")
