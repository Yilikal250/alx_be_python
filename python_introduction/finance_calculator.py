# Prompt user to enter monthly income
monthly_income = float (input("Enter your monthly income: "))

# Prompt user to enter total monthly expenses
monthly_expense = float (input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expense

# Calculate projected savings after one year with 5% interest
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

# Print the monthly savings
print("Your monthly savings are $" + str(monthly_savings) + ".")

# Print the projected savings after one year with interest
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")