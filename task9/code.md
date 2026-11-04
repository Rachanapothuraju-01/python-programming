# 9. Multi-Currency Travel Budget Analysis

## 1. Problem Statement

Develop a Python program for a Multi-Currency Travel Budget Analysis System. The program converts travel expenses from different currencies into a common base currency using supplied exchange rates.

The program should include currency conversion fees, calculate total travel expenses, compare planned spending against the available budget, and identify the largest expense category.

Finally, generate a travel budget report displaying converted expenses, conversion fees, total spending, remaining budget, and the largest expense category.

## 2. Algorithm

1. Start the program.
2. Enter the travel budget in the base currency.
3. Enter the number of expense categories.
4. Enter the expense category name.
5. Enter the expense amount in foreign currency.
6. Enter the currency exchange rate.
7. Enter the currency conversion fee percentage.
8. Convert the foreign currency amount into the base currency.
9. Calculate the conversion fee.
10. Calculate the total expense including the fee.
11. Repeat the process for all expense categories.
12. Calculate the total travel expenses.
13. Identify the largest expense category.
14. Compare total expenses with the available budget.
15. Calculate the remaining budget or excess spending.
16. Display the final travel budget report.
17. Stop the program.

## 3. Flowchart
```mermaid
flowchart TD
    A([Start]) --> B[Enter Travel Budget]
    B --> C[Enter Number of Expenses]
    C --> D[Enter Expense Category]
    D --> E[Enter Foreign Currency Amount]
    E --> F[Enter Exchange Rate and Fee]
    F --> G[Convert Amount to Base Currency]
    G --> H[Calculate Conversion Fee]
    H --> I[Calculate Total Expense]
    I --> J[Store Expense Details]
    J --> K{More Expenses?}
    K -- Yes --> D
    K -- No --> L[Calculate Total Spending]
    L --> M[Identify Largest Expense Category]
    M --> N{Spending <= Budget?}
    N -- Yes --> O[Calculate Remaining Budget]
    N -- No --> P[Calculate Excess Spending]
    O --> Q[Display Final Budget Report]
    P --> Q
    Q --> R([Stop])
```
4. Sample Input
Enter total travel budget in INR: 100000

Enter number of expense categories: 4

Expense Category 1
Enter category name: Hotel
Enter expense amount: 200
Enter exchange rate to INR: 90
Enter conversion fee percentage: 2

Expense Category 2
Enter category name: Food
Enter expense amount: 100
Enter exchange rate to INR: 90
Enter conversion fee percentage: 2

Expense Category 3
Enter category name: Transport
Enter expense amount: 150
Enter exchange rate to INR: 90
Enter conversion fee percentage: 2

Expense Category 4
Enter category name: Shopping
Enter expense amount: 300
Enter exchange rate to INR: 90
Enter conversion fee percentage: 2
===== FINAL TRAVEL EXPENSE REPORT =====
5. Sample Output
Category: Hotel
Original Amount: 200.0
Converted Amount: Rs. 18000.0
Conversion Fee: Rs. 360.0
Total Expense: Rs. 18360.0

Category: Food
Original Amount: 100.0
Converted Amount: Rs. 9000.0
Conversion Fee: Rs. 180.0
Total Expense: Rs. 9180.0

Category: Transport
Original Amount: 150.0
Converted Amount: Rs. 13500.0
Conversion Fee: Rs. 270.0
Total Expense: Rs. 13770.0

Category: Shopping
Original Amount: 300.0
Converted Amount: Rs. 27000.0
Conversion Fee: Rs. 540.0
Total Expense: Rs. 27540.0

Total Travel Expense: Rs. 68850.0

Planned Budget: Rs. 100000.0

Largest Expense Category: Shopping

Remaining Budget: Rs. 31150.0

Status: Within Budget

Travel Budget Analysis Completed.
