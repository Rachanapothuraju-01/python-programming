# Student Performance Trend Analysis Using Python

## 1. Problem Statement

Develop a Python program to analyze student performance across multiple examinations. The program should accept student marks in different subjects for multiple examinations, compare assessment scores, calculate improvements and declines, identify consistently weak subjects, and classify students based on their academic performance.

The system should:

- Accept student details and examination marks.
- Calculate the total and average marks for each examination.
- Compare marks between examinations.
- Identify improvement or decline in student performance.
- Identify subjects in which students consistently score low marks.
- Classify students into different performance categories based on their average marks.

## 2. Algorithm

1. Start the program.
2. Read the number of students and subjects.
3. Read student names and subject names.
4. Enter marks obtained by each student in the first examination.
5. Enter marks obtained in the second examination.
6. Calculate the total and average marks for both examinations.
7. Calculate the improvement or decline in marks for each subject.
8. Identify consistently weak subjects by checking whether marks are below 40 in both examinations.
9. Classify students based on their average marks:
   - 90 and above – Excellent
   - 75 to 89 – Very Good
   - 60 to 74 – Good
   - 40 to 59 – Average
   - Below 40 – Poor
10. Display the performance analysis and classification.
11. Stop the program.

## 3. Flowchart
``` mermaid
          START
            |
            v
     Input Student Details
            |
            v
     Input Subject Names
            |
            v
   Enter Exam 1 and Exam 2 Marks
            |
            v
    Calculate Total and Average
            |
            v
     Compare Examination Marks
            |
            v
   Identify Weak Subjects
            |
            v
    Classify Student Performance
            |
            v
      Display Analysis
            |
            v
           STOP
```


```

## 4. Sample Input

text

```text
Enter student name: Rahul

Enter marks for First Examination:
Python: 65
Mathematics: 35
English: 70
Science: 45

Enter marks for Second Examination:
Python: 80
Mathematics: 38
English: 75
Science: 60
```

## 5. Sample Output

text

```text
----- PERFORMANCE ANALYSIS -----

Student Name: Rahul

Subject-wise Performance:

Python : 15 - Improved
Mathematics : 3 - Improved
English : 5 - Improved
Science : 15 - Improved

Consistently Weak Subjects:
Mathematics

First Exam Total: 215
Second Exam Total: 253

First Exam Average: 53.75
Second Exam Average: 63.25

Overall Trend: Improved

Student Classification:
Good
```

## 6. Result

Thus, the Python program for Student Performance Trend Analysis was successfully developed and executed. It compares examination marks, calculates improvements and declines, identifies consistently weak subjects, and classifies students based on their academic performance.
