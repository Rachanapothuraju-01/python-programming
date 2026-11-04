# Progressive Water Tariff Analysis – Python Program

## 1. Problem Statement

Develop a Python program to calculate water bills for multiple households based on their monthly water consumption. The program should apply different water tariff rates for different consumption slabs, add fixed charges and penalties for excessive water usage, and calculate the total bill for each household. It should also compare the consumption patterns of all households and identify households with excessive water usage.

## 2. Algorithm
1. Start the program.
2. Read the number of households.
3. Set the water consumption slab rates.
4. Set the fixed fee and excessive usage penalty.
5. Read the household name and water consumption.
6. Calculate the water charges based on consumption slabs.
7. Add the fixed fee to the water charges.
8. Check whether consumption exceeds the allowed limit.
9. If consumption exceeds the limit, add the penalty.
10. Calculate the total water bill.
11. Display the household name, consumption, and total bill.
12. Compare the consumption of all households.
13. Identify and display households with excessive water usage.
14. Stop the program.
```

## 3. Sample Input

```
Enter number of households: 3

Household 1
Enter household name: Ravi
Enter water consumption in litres: 80

Household 2
Enter household name: Rani
Enter water consumption in litres: 250

Household 3
Enter household name: Kumar
Enter water consumption in litres: 400
```

## 45. Sample Output

```
Household Name: Ravi
Water Consumption: 80.0 litres
Water Charge: Rs. 80.0
Fixed Fee: Rs. 50
Penalty: Rs. 0
Total Bill: Rs. 130.0
Usage Status: Normal Usage

Household Name: Rani
Water Consumption: 250.0 litres
Water Charge: Rs. 450.0
Fixed Fee: Rs. 50
Penalty: Rs. 0
Total Bill: Rs. 500.0
Usage Status: Normal Usage

Household Name: Kumar
Water Consumption: 400.0 litres
Water Charge: Rs. 1000.0
Fixed Fee: Rs. 50
Penalty: Rs. 100
Total Bill: Rs. 1150.0
Usage Status: Excessive Usage

Water Tariff Analysis Completed
```

## 5. Flowchart
```meramid
flowchart TD
    A([Start]) --> B[/Enter number of households/]
    B --> C[Set fixed fee, slab rates and penalty]
    C --> D[/Enter household name and water consumption/]
    D --> E{Consumption <= 100?}
    E -- Yes --> F[Calculate charge at Rs.1 per litre]
    E -- No --> G{Consumption <= 200?}
    G -- Yes --> H[Calculate first 100 at Rs.1 and remaining at Rs.2]
    G -- No --> I{Consumption <= 300?}
    I -- Yes --> J[Calculate first 100 at Rs.1, next 100 at Rs.2 and remaining at Rs.3]
    I -- No --> K[Calculate first 300 slabs and remaining at Rs.4]
    F --> L[Add fixed fee]
    H --> L
    J --> L
    K --> L
    L --> M{Consumption > 300?}
    M -- Yes --> N[Add penalty]
    M -- No --> O[No penalty]
    N --> P[Calculate total bill]
    O --> P
    P --> Q[/Display bill and usage status/]
    Q --> R{More households?}
    R -- Yes --> D
    R -- No --> S([Stop])
```
## 6. Water Tariff Slab Details

| Consumption          | Rate     |
| -------------------- | -------- |
| First 100 litres     | ₹1/litre |
| 101–200 litres       | ₹2/litre |
| 201–300 litres       | ₹3/litre |
| Above 300 litres     | ₹4/litre |
| Fixed fee            | ₹50      |
| Excess usage penalty | ₹100     |

Note: These are assumed rates for this Python assignment, not official water tariff rates.

Conclusion: This program calculates progressive water bills, applies penalties for excessive consumption, and helps compare water usage among multiple households.
