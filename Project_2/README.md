# Tip Calculator 💸

A simple and fun program to calculate the amount each person needs to pay when splitting a bill, including tips!

## How It Works

1. **💰 Input the total bill amount.**
2. **🍽️ Decide the tip percentage you want to give (e.g., 10%, 12%, or 15%).**
3. **👫 Enter the number of people sharing the bill.**
4. **🔢 The program calculates the total amount per person, including the tip.**

## Usage

Run the program and follow the prompts:

```python
# What was the total bill?
bill = float(input("What was the total bill? $"))

# How much tip would you like to give? 10, 12, or 15?
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))

# How many people to split the bill?
people = int(input("How many people to split the bill? "))

# Calculate the total tip amount
tip_amount = bill * (tip_percentage / 100)

# Calculate the total amount to be paid
total_amount = bill + tip_amount

# Calculate the amount each person should pay
amount_per_person = total_amount / people

# Output the result
print(f"Each person should pay: ${amount_per_person:.2f}")
```
## 🛠️ OR

1. **Clone or Download** this repository.  
2. Make sure **Python** is installed on your system.  
3. Open your **terminal or command prompt**.  
4. Navigate to the directory where the script is saved.  
5. Run the following command:  
   ```bash
   python Tip_Calculator.py


## Output Example 🍽️💵
```plaintext
What was the total bill? $100
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 4
Each person should pay: $28.00
```
## ⚡ Why This Project?

This project is part of Angela Yu’s Python course on Udemy. It's a beginner-friendly exercise to learn how to handle user inputs and outputs in Python.

This Tip Calculator is a beginner-friendly way to practice:

📝 Taking user input  
🔢 Performing basic calculations  
💡 Using variables and `f-strings`



