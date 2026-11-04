
# Integrated E-Commerce Order Processing
# and Reconciliation System

products = {
    101: {"name": "Laptop", "price": 50000, "stock": 10},
    102: {"name": "Mobile", "price": 20000, "stock": 15},
    103: {"name": "Headphones", "price": 2000, "stock": 20}
}

total_revenue = 0
total_orders = 0

n = int(input("Enter number of orders: "))

for i in range(n):

    print("\nOrder", i + 1)

    pid = int(input("Enter Product ID: "))
    qty = int(input("Enter Order Quantity: "))

    if pid not in products:
        print("Invalid Product ID")
        continue

    product = products[pid]

    if qty <= 0 or qty > product["stock"]:
        print("Invalid quantity or insufficient stock")
        continue

    # Calculate amount and discount
    amount = qty * product["price"]

    if amount >= 50000:
        discount = amount * 0.10
    elif amount >= 20000:
        discount = amount * 0.05
    else:
        discount = 0

    final_amount = amount - discount

    # Dispatch details
    dispatched = int(input("Enter dispatched quantity: "))
    returned = int(input("Enter returned quantity: "))

    if dispatched < 0 or dispatched > qty:
        print("Invalid dispatch quantity")
        continue

    if returned < 0 or returned > dispatched:
        print("Invalid return quantity")
        continue

    # Update stock
    products[pid]["stock"] -= dispatched
    products[pid]["stock"] += returned

    # Calculate revenue for completed sales
    sold_qty = dispatched - returned
    revenue = sold_qty * product["price"]

    if qty != dispatched:
        print("Discrepancy: Ordered and dispatched quantities differ")

    if returned > 0:
        print("Return detected:", returned)

    total_revenue += revenue - (discount * sold_qty / qty)
    total_orders += 1

    print("Product:", product["name"])
    print("Order Amount: Rs.", amount)
    print("Discount: Rs.", discount)
    print("Final Order Amount: Rs.", final_amount)
    print("Dispatched:", dispatched)
    print("Returned:", returned)
    print("Sold Quantity:", sold_qty)
    print("Revenue: Rs.", revenue)

# Final summary
print("\n----- FINAL SUMMARY -----")

print("Total Processed Orders:", total_orders)
print("Total Revenue: Rs.", round(total_revenue, 2))

print("\n----- INVENTORY SUMMARY -----")

for pid, details in products.items():
    print("Product ID:", pid)
    print("Product Name:", details["name"])
    print("Available Stock:", details["stock"])

print("\nOrder Processing Completed.")

