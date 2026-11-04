# Integrated E-Commerce Order Processing and Reconciliation – Python Program

## 1. Problem Statement

Develop a Python program for an Integrated E-Commerce Order Processing and Reconciliation System.

The system processes customer product orders, calculates discounts, manages product dispatches, handles product returns, and updates stock quantities.

The program should:

1. Accept product details, prices, and quantities.
2. Calculate the total order amount.
3. Apply discounts based on the order value.
4. Process product dispatches and update inventory.
5. Handle product returns and restore stock.
6. Calculate total revenue after discounts and returns.
7. Identify discrepancies between ordered, dispatched, and returned quantities.
8. Generate a final inventory and revenue summary.

## 2. Algorithm

1. Start the program.
2. Enter the number of products.
3. Input product name, price, initial stock, and order quantity.
4. Calculate the total order amount.
5. Apply discounts based on the total amount.
6. Calculate the final order amount.
7. Check whether sufficient stock is available.
8. If stock is available, dispatch the products.
9. Update the available stock.
10. Enter the returned quantity.
11. Add returned products back to inventory.
12. Calculate the final revenue.
13. Compare ordered, dispatched, and returned quantities.
14. Identify any discrepancies.
15. Display the final inventory summary.
16. Stop the program.

```

## 3. Sample Input

```mermaid
Enter number of products: 2

Product 1
Enter product name: Laptop
Enter product price: 50000
Enter available stock: 10
Enter order quantity: 2
Enter returned quantity: 1

Product 2
Enter product name: Mouse
Enter product price: 1000
Enter available stock: 20
Enter order quantity: 3
Enter returned quantity: 0
```

## 4. Sample Output

```
===== E-COMMERCE FINAL REPORT =====

Product: Laptop
Ordered Quantity: 2
Dispatched Quantity: 2
Returned Quantity: 1
Remaining Stock: 9
Discount: Rs. 10000.0
Revenue: Rs. 50000.0
Status: Return Processed

Product: Mouse
Ordered Quantity: 3
Dispatched Quantity: 3
Returned Quantity: 0
Remaining Stock: 17
Discount: Rs. 0.0
Revenue: Rs. 3000.0
Status: No Discrepancy

Total Discount: Rs. 10000.0
Total Revenue: Rs. 53000.0

===== INVENTORY SUMMARY =====
Laptop : 9 units
Mouse : 17 units

Order reconciliation completed.
```

## 5. Flowchart
```mermaid
    A([Start]) --> B[/Enter number of products/]
    B --> C[/Enter product details/]
    C --> D[Calculate total order amount]
    D --> E{Check order amount}
    E -->|Above 5000| F[Apply 10% discount]
    E -->|2000 to 4999| G[Apply 5% discount]
    E -->|Below 2000| H[No discount]
    F --> I[Calculate final amount]
    G --> I
    H --> I
    I --> J{Stock available?}
    J -->|No| K[Dispatch zero quantity]
    J -->|Yes| L[Dispatch products]
    K --> M[Enter returned quantity]
    L --> M
    M --> N{Valid return?}
    N -->|No| O[Set return quantity to zero]
    N -->|Yes| P[Update stock]
    O --> P
    P --> Q[Calculate revenue]
    Q --> R[Check discrepancies]
    R --> S{More products?}
    S -->|Yes| C
    S -->|No| T[Generate final inventory report]
    T --> U[Display total revenue and discount]
    U --> V([Stop])
```

## 7. Result

The Integrated E-Commerce Order Processing and Reconciliation Python program successfully processes product orders, calculates discounts, manages dispatches and returns, updates inventory, identifies discrepancies, and generates the final revenue and stock summary.

Note: The sample program assumes that the discount is calculated on the full ordered quantity. Revenue is calculated on the quantity retained by the customer. The program can be extended to calculate discounts only on successfully dispatched products.
