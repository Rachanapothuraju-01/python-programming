# Advanced String-Based Registration Record Analyzer – Python Program

## 1. Problem Statement

Develop a Python program to analyze registration records stored as structured strings. The program should:

1. Read multiple registration records.
2. Split each record into separate fields.
3. Validate the length and format of each field.
4. Extract registration ID, name, email, and phone number.
5. Detect duplicate registration IDs.
6. Classify errors such as invalid ID, invalid name, invalid email, invalid phone number, and duplicate records.
7. Display valid records and error classifications.

## 2. Algorithm

1. Start the program.
2. Initialize an empty list to store registration IDs.
3. Read the number of registration records.
4. Read each registration record as a string.
5. Split the string using the comma separator.
6. Check whether the record contains four fields.
7. Extract ID, name, email, and phone number.
8. Validate each field:
   - ID must contain 5 characters.
   - Name must contain at least 3 characters.
   - Email must contain `@` and `.`.
   - Phone number must contain exactly 10 digits.
9. Check whether the registration ID already exists.
10. If the ID is repeated, classify it as a duplicate.
11. Display valid records and error messages.
12. Stop the program.



## 5. Flowchart
```mermaid

flowchart TD
    A([Start]) --> B[Initialize Registration ID List]
    B --> C[/Enter Number of Records/]
    C --> D[/Read Registration Record/]
    D --> E[Split Record into Fields]
    E --> F{Are There 4 Fields?}

    F -- No --> G[Display Invalid Fields Error]
    G --> N{More Records?}

    F -- Yes --> H[Extract ID, Name, Email and Phone]
    H --> I[Validate Field Lengths and Formats]
    I --> J{Is ID Already Present?}

    J -- Yes --> K[Add Duplicate ID Error]
    J -- No --> L[Store Registration ID]

    K --> M{Are There Any Errors?}
    L --> M

    M -- No --> O[Display Valid Registration]
    M -- Yes --> P[Display Error Classification]

    O --> N
    P --> N

    N -- Yes --> D
    N -- No --> Q[Display Analysis Completed]
    Q --> R([Stop])
## 3. Sample Input

```
Enter number of records: 3

Enter Registration Record 1
ID,Name,Email,Phone: R1001,Ravi,ravi@gmail.com,9876543210

Enter Registration Record 2
ID,Name,Email,Phone: R1002,Anu,anuemail.com,987654321

Enter Registration Record 3
ID,Name,Email,Phone: R1001,Raju,raju@gmail.com,9876543210
```

## 4. Sample Output

```
Registration Successful
ID: R1001
Name: Ravi
Email: ravi@gmail.com
Phone: 9876543210

Registration Failed
Error Classification: Invalid Email, Invalid Phone

Registration Failed
Error Classification: Duplicate ID

Registration Analysis Completed
```




