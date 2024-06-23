# Prompt user to enter monthly income
Monthly_Income = float(input("Enter your monthly income: "))

# Prompt user to enter total monthly expenses
Monthly_Expense = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
Monthly_Savings = Monthly_Income - Monthly_Expense

# Calculate projected savings after one year with 5% interest
Projected_Savings = Monthly_Savings * 12 + (Monthly_Savings * 12 * 0.05)

# Print the monthly savings
print("Your monthly savings are $" + str(Monthly_Savings) + ".")

# Print the projected savings after one year with interest
print("Projected savings after one year, with interest, is: $" + str(Projected_Savings) + ".")