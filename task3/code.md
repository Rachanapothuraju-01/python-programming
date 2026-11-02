

## 1. Problem Statement

Develop a Python program for Campus Event Financial Planning. The program calculates the total expenses of organizing a college event, including venue, equipment, catering, transport, and certificate costs. It determines the participant contribution, calculates sponsorship shortfalls, and finds the minimum number of registrations required to break even.

## 2. Algorithm

1. Start the program.
2. Read the venue cost.
3. Read the equipment cost.
4. Read the catering cost.
5. Read the transport cost.
6. Read the certificate cost.
7. Read the sponsorship amount.
8. Read the cost per participant.
9. Read the contribution per participant.
10. Calculate the total event expenses.
11. Calculate the sponsorship shortfall.
12. Calculate the remaining amount after sponsorship.
13. Calculate the minimum registration count required to break even.
14. Display the total expenses, sponsorship shortfall, participant contribution, and minimum registrations.
15. Stop the program.



## 3. Sample Input

```
Enter venue cost: 10000
Enter equipment cost: 5000
Enter catering cost: 8000
Enter transport cost: 4000
Enter certificate cost: 3000
Enter sponsorship amount: 10000
Enter catering cost per participant: 100
Enter contribution per participant: 300
```

## 4. Sample Output

```
----- CAMPUS EVENT FINANCIAL REPORT -----

Total Event Cost: 30000.0
Sponsorship Amount: 10000.0
Sponsorship Shortfall: 20000.0
Remaining Amount: 20000.0
Minimum Registrations Required: 100
Participant Contribution: 300.0
```

Explanation:

- Total event cost = ₹30,000
- Sponsorship = ₹10,000
- Remaining amount = ₹20,000
- Contribution per participant = ₹300
- Catering cost per participant = ₹100
- Amount available per participant towards fixed costs = ₹200
- Minimum registrations = 20,000 ÷ 200 = 100 participants

## 5. Flowchart (Mermaid)
```meramid

flowchart TD
    A([Start]) --> B[/Enter venue cost/]
    B --> C[/Enter equipment cost/]
    C --> D[/Enter catering cost/]
    D --> E[/Enter transport cost/]
    E --> F[/Enter certificate cost/]
    F --> G[/Enter sponsorship amount/]
    G --> H[/Enter participant cost and contribution/]
    H --> I[Calculate total event cost]
    I --> J[Calculate sponsorship shortfall]
    J --> K[Calculate remaining amount]
    K --> L{Contribution > Participant Cost?}
    L -- Yes --> M[Calculate minimum registrations]
    L -- No --> N[Break-even not possible]
    M --> O[/Display financial report/]
    N --> O
    O --> P([Stop])
```


## 6. Break-Even Concept

Revenue

Total cost

Loss

Profit

10203040506050010001500Quantity$Q\*

\\(Q^\*=\frac{F}{p-v}=\frac{\text{600}}{\text{35}-\text{15}}=\text{30}\\)

Q\* is the break-even quantity where total revenue matches total cost.

\\(F\\)

$

\\(v\\)

$/unit

\\(p\\)

$/unit

Give feedback

Note: This program assumes venue, equipment, catering, transport and certificate amounts entered initially are fixed event expenses. The catering cost per participant is treated as an additional variable cost. The calculation finds the minimum registrations needed to cover costs after sponsorship.
