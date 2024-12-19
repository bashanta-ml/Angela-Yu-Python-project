# Tip Calculator – Let's make math fun!
print("Welcome to the Tip Calculator!")

# Total bill input
bill = float(input("What was the total bill? $"))

# Tip choice: 10, 12, or 15%
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))

# Number of people to split the bill
people = int(input("How many people to split the bill? "))

# Calculate the tip as a decimal
tip_as_percentage = tip / 100

# Total tip amount
total_tip_amount = bill * tip_as_percentage

# Total bill (bill + tip)
total_bill = bill + total_tip_amount

# Split the total bill
bill_per_person = total_bill / people

# Round the final amount
final_amount = round(bill_per_person, 2)

# Output the result
print(f"Each person should pay: ${final_amount}")
