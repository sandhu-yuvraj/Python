amount = float(input("Enter the amount of bill in dollars: "))
tip_percentage = float(input("Enter the tip percentage: ")) #write without the % sign
tip = amount * tip_percentage / 100
print("Tip amount: $", tip)