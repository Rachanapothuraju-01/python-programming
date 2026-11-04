
# Campus Event Financial Planning

print("===== CAMPUS EVENT FINANCIAL PLANNING =====")

# Input fixed expenses
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
transport = float(input("Enter transportation cost: "))

# Input variable expenses
catering = float(input("Enter catering cost per participant: "))
certificate = float(input("Enter certificate cost per participant: "))

# Input participant details
participants = int(input("Enter expected number of participants: "))
registration_fee = float(input("Enter registration fee per participant: "))

# Input sponsorship
sponsorship = float(input("Enter sponsorship amount: "))

# Calculate costs
fixed_cost = venue + equipment + transport

variable_cost = catering + certificate

total_variable_cost = variable_cost * participants

total_cost = fixed_cost + total_variable_cost

# Calculate income
participant_contribution = participants * registration_fee

total_income = participant_contribution + sponsorship

# Calculate sponsorship shortfall
shortfall = max(0, total_cost - total_income)

# Calculate break-even registrations
contribution_per_person = registration_fee - variable_cost

if contribution_per_person > 0:
    required = (fixed_cost - sponsorship) / contribution_per_person
    minimum_registrations = max(0, int(required) +
                                (1 if required > int(required) else 0))
else:
    minimum_registrations = None

# Calculate profit or loss
profit_loss = total_income - total_cost

# Display report
print("\n===== EVENT FINANCIAL REPORT =====")

print("Fixed Cost: Rs.", fixed_cost)
print("Variable Cost: Rs.", variable_cost)
print("Total Variable Cost: Rs.", total_variable_cost)
print("Total Event Cost: Rs.", total_cost)

print("\nParticipant Contribution: Rs.", participant_contribution)
print("Sponsorship Amount: Rs.", sponsorship)
print("Total Income: Rs.", total_income)

print("Sponsorship Shortfall: Rs.", shortfall)

if minimum_registrations is not None:
    print("Minimum Registrations Required:",
          minimum_registrations)
else:
    print("Break-even is not possible with the given fee.")

print("Profit / Loss: Rs.", profit_loss)

if profit_loss > 0:
    print("Result: Event is in Profit")
elif profit_loss < 0:
    print("Result: Event is in Loss")
else:
    print("Result: Event is at Break-even")

print("\nFinancial Planning Completed.")

