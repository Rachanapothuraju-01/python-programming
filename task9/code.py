
# Multi-Currency Travel Budget Analysis

print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")

budget = float(input("Enter travel budget (INR): "))

n = int(input("Enter number of expense categories: "))

expenses = []
total_spending = 0

# Process expenses
for i in range(n):

    print("\nExpense", i + 1)

    category = input("Enter expense category: ")

    amount = float(input("Enter foreign currency amount: "))

    rate = float(input("Enter exchange rate (INR): "))

    fee_percent = float(input("Enter conversion fee percentage: "))

    if amount < 0 or rate <= 0 or fee_percent < 0:
        print("Invalid expense details!")
        continue

    # Currency conversion
    converted_amount = amount * rate

    # Calculate conversion fee
    fee = converted_amount * fee_percent / 100

    # Total expense
    total_amount = converted_amount + fee

    total_spending += total_amount

    expenses.append({
        "category": category,
        "converted": converted_amount,
        "fee": fee,
        "total": total_amount
    })

# Find largest expense category
if expenses:
    largest = max(expenses, key=lambda x: x["total"])
else:
    largest = None

# Display expense details
print("\n========== TRAVEL EXPENSE REPORT ==========")

for expense in expenses:

    print("\nCategory:", expense["category"])
    print("Converted Amount: Rs.", round(expense["converted"], 2))
    print("Conversion Fee: Rs.", round(expense["fee"], 2))
    print("Total Expense: Rs.", round(expense["total"], 2))

# Budget calculation
print("\n========== FINAL BUDGET SUMMARY ==========")

print("Travel Budget: Rs.", budget)
print("Total Spending: Rs.", round(total_spending, 2))

if total_spending <= budget:

    remaining = budget - total_spending

    print("Remaining Budget: Rs.", round(remaining, 2))
    print("Status: Within Budget")

else:

    excess = total_spending - budget

    print("Excess Spending: Rs.", round(excess, 2))
    print("Status: Budget Exceeded")

if largest:
    print("Largest Expense Category:", largest["category"])
    print("Largest Expense Amount: Rs.", round(largest["total"], 2))

print("\nTravel Budget Analysis Completed.")

