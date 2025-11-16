print(" Tip Calculator")

bill = float(input("Enter total bill amount: ₹"))
tip_percent = int(input("Enter tip percentage: "))
people = int(input("How many people to split the bill? "))

tip = bill * (tip_percent / 100)
total = bill + tip
each = total / people

print(f"\nTotal bill (with tip): ₹{round(total, 2)}")
print(f"Each person should pay: ₹{round(each, 2)}")
