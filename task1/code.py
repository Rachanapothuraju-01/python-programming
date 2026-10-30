

# Employee Payroll and Deduction Analysis

# Get employee details
name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")

# Get salary details
basic = float(input("Enter Basic Pay: "))
allowances = float(input("Enter Allowances: "))
overtime = float(input("Enter Overtime: "))
incentives = float(input("Enter Incentives: "))

# Calculate Gross Salary
gross = basic + allowances + overtime + incentives

# Calculate Progressive Deduction
if gross <= 20000:
    deduction_rate = 0.05
elif gross <= 40000:
    deduction_rate = 0.10
else:
    deduction_rate = 0.15

deduction = gross * deduction_rate

# Calculate Net Salary
net_salary = gross - deduction

# Display Salary Statement
print("\n===== EMPLOYEE SALARY STATEMENT =====")
print("Employee Name :", name)
print("Employee ID   :", emp_id)
print("Basic Pay     :", basic)
print("Allowances    :", allowances)
print("Overtime      :", overtime)
print("Incentives    :", incentives)
print("------------------------------------")
print("Gross Salary  :", gross)
print("Deduction     :", deduction)
print("Net Salary    :", net_salary)
print("====================================")
