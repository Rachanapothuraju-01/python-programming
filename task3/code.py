
# Campus Event Financial Planning

# Input costs
venue = float(input("Enter venue cost: "))
equipment = float(input("Enter equipment cost: "))
catering = float(input("Enter catering cost: "))
transport = float(input("Enter transport cost: "))
certificates = float(input("Enter certificate cost: "))

sponsorship = float(input("Enter sponsorship amount: "))
cost_per_person = float(input("Enter catering cost per participant: "))
contribution = float(input("Enter contribution per participant: "))

# Calculate fixed expenses
total_cost = venue + equipment + catering + transport + certificates

# Calculate sponsorship shortfall
if sponsorship < total_cost:
    shortfall = total_cost - sponsorship
else:
    shortfall = 0

# Calculate remaining amount after sponsorship
remaining = max(0, total_cost - sponsorship)

# Calculate minimum registrations
if contribution > cost_per_person:
    minimum_registrations = int(
        remaining / (contribution - cost_per_person)
    )
    if remaining % (contribution - cost_per_person) != 0:
        minimum_registrations += 1
else:
    minimum_registrations = 0

# Display results
print("\n----- CAMPUS EVENT FINANCIAL REPORT -----")
print("Total Event Cost:", total_cost)
print("Sponsorship Amount:", sponsorship)
print("Sponsorship Shortfall:", shortfall)
print("Remaining Amount:", remaining)

if contribution > cost_per_person:
    print("Minimum Registrations Required:",
          minimum_registrations)
else:
    print("Break-even is not possible with the given contribution.")

print("Participant Contribution:", contribution)

