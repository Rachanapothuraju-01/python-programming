
# Manufacturing Cost and Profitability Analysis

print("MANUFACTURING COST ANALYSIS")

# Input details
product = input("Enter product name: ")

quantity = int(input("Enter production quantity: "))

material_cost = float(input("Enter raw material cost: "))

labour_cost = float(input("Enter labour charges: "))

wastage_percent = float(input("Enter wastage percentage: "))

machine_cost = float(input("Enter machine operating cost: "))

selling_price = float(input("Enter selling price per unit: "))

profit_target = float(input("Enter profit target: "))

# Calculate wastage cost
wastage_cost = material_cost * wastage_percent / 100

# Calculate total manufacturing cost
total_cost = (
    material_cost +
    labour_cost +
    wastage_cost +
    machine_cost
)

# Calculate cost per unit
cost_per_unit = total_cost / quantity

# Calculate revenue
total_revenue = selling_price * quantity

# Calculate profit
profit = total_revenue - total_cost

# Calculate profit percentage
profit_percentage = (profit / total_cost) * 100

# Display results
print("\n===== MANUFACTURING REPORT =====")

print("Product Name:", product)
print("Production Quantity:", quantity)

print("Material Cost: Rs.", material_cost)
print("Labour Cost: Rs.", labour_cost)
print("Wastage Cost: Rs.", wastage_cost)
print("Machine Cost: Rs.", machine_cost)

print("Total Manufacturing Cost: Rs.", total_cost)

print("Cost Per Unit: Rs.", round(cost_per_unit, 2))

print("Selling Price Per Unit: Rs.", selling_price)

print("Total Revenue: Rs.", total_revenue)

print("Total Profit: Rs.", profit)

print("Profit Percentage:", round(profit_percentage, 2), "%")

# Check profit target
if profit >= profit_target:
    print("Result: Profit Target Achieved")
else:
    print("Result: Profit Target Not Achieved")

print("\nAnalysis Completed.")

