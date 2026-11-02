
print("===== RETAIL BILLING SYSTEM =====")

n = int(input("Enter number of products: "))

products = []
subtotal = 0
total_tax = 0

for i in range(n):
    print("\nEnter Product", i + 1)

    name = input("Product Name: ")
    quantity = int(input("Quantity: "))
    price = float(input("Price per unit: "))
    category = input("Category (food/clothing/electronics): ").lower()

    amount = quantity * price

    # Category-specific tax rates
    if category == "food":
        tax_rate = 5
    elif category == "clothing":
        tax_rate = 12
    elif category == "electronics":
        tax_rate = 18
    else:
        tax_rate = 10

    products.append(
        [name, quantity, price, category,
         amount, tax_rate]
    )

    subtotal += amount

# Discount calculation
if subtotal > 5000:
    discount_rate = 10
elif subtotal > 3000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100

# Maximum concession limit
if discount > 500:
    discount = 500

# Calculate tax after distributing discount
for product in products:
    amount = product[4]

    if subtotal > 0:
        item_discount = discount * amount / subtotal
    else:
        item_discount = 0

    taxable_amount = amount - item_discount

    tax = taxable_amount * product[5] / 100

    total_tax += tax

# Final bill
final_amount = subtotal - discount + total_tax

# Display invoice
print("\n========== ITEMIZED INVOICE ==========")
print("Product\tQty\tPrice\tAmount\tTax")

for product in products:
    print(product[0], "\t",
          product[1], "\t",
          product[2], "\t",
          product[4], "\t",
          str(product[5]) + "%")

print("--------------------------------------")
print("Subtotal       : Rs.", round(subtotal, 2))
print("Discount       : Rs.", round(discount, 2))
print("Total Tax      : Rs.", round(total_tax, 2))
print("--------------------------------------")
print("FINAL BILL     : Rs.", round(final_amount, 2))
print("======================================")

