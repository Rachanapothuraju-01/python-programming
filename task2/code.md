# Retail Billing with Multiple Discount Rules

## 1. Problem Statement

Develop a Python program for a retail billing system that processes multiple products purchased by a customer. The program should accept product name, quantity, price, and category-specific tax rates.

It should calculate the total price of each product, apply discounts based on purchase thresholds, and ensure that the total discount does not exceed the maximum concession limit. Finally, generate an itemized invoice showing product details, subtotal, discount, tax amount, and final bill amount.

## 2. Algorithm

1. Start the program.
2. Read the number of products.
3. For each product, input:
   - Product name
   - Quantity
   - Price per unit
   - Category
   - Tax percentage
4. Calculate the product amount using quantity × price.
5. Calculate the subtotal of all products.
6. Apply discount rules:
   - If subtotal is above ₹5000, give 10% discount.
   - If subtotal is above ₹3000, give 5% discount.
   - Otherwise, no discount.
7. Apply the maximum concession limit of ₹500.
8. Calculate the taxable amount after discount.
9. Calculate category-specific tax.
10. Calculate the final bill amount.
11. Display the itemized invoice.
12. Stop the program.



## 3. Sample Input

```
Enter number of products: 3

Enter Product 1
Product Name: Rice
Quantity: 2
Price per unit: 1000
Category: food

Enter Product 2
Product Name: Shirt
Quantity: 2
Price per unit: 800
Category: clothing

Enter Product 3
Product Name: Laptop
Quantity: 1
Price per unit: 3000
Category: electronics
```

## 4. Sample Output

```
===== RETAIL BILLING SYSTEM =====

========== ITEMIZED INVOICE ==========

Product   Qty   Price   Amount   Tax
Rice       2    1000    2000     5%
Shirt      2     800    1600     12%
Laptop     1    3000    3000     18%

--------------------------------------
Subtotal       : Rs. 6600.00
Discount       : Rs. 500.00
Total Tax      : Rs. 964.24
--------------------------------------
FINAL BILL     : Rs. 7064.24
======================================
```

## 5. Flowchart

Mermaid Flowchart
```meramid

flowchart TD
    A([Start]) --> B[/Enter number of products/]
    B --> C[/Enter product name, price, quantity and category/]
    C --> D[Calculate subtotal for each product]
    D --> E[Calculate category-specific tax]
    E --> F[Calculate total bill amount]
    F --> G{Is bill amount above discount threshold?}
    G -- Yes --> H[Calculate eligible discount]
    G -- No --> I[Set discount to zero]
    H --> J{Is discount above maximum concession?}
    J -- Yes --> K[Apply maximum concession limit]
    J -- No --> L[Apply calculated discount]
    K --> M[Calculate final bill]
    L --> M
    I --> M
    M --> N[Generate itemized invoice]
    N --> O[/Display subtotal, tax, discount and final amount/]
    O --> P([End])
```


## 7. Expected Result

The program successfully calculates the retail bill for multiple products by applying category-specific taxes, threshold-based discounts, and maximum concession limits. It displays the subtotal, discount, tax, and final payable amount in an itemized invoice.

Note: The tax rates and discount limits used here are sample values for the assignment. Actual rates can be changed according to the requirements.
