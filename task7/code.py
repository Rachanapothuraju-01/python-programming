
# Retail Billing with Multiple Discount Rules

products = []

# Category-specific tax rates
tax_rates = {
    "food": 5,
    "clothing": 12,
    "electronics": 18
}

n = int(input("Enter number of products: "))

subtotal = 0
total_tax = 0

# Enter product details
for i in range(n):

    print("\nProduct", i + 1)

    name = input("Enter product name: ")
    category = input("Enter category (food/clothing/electronics): ").lower()
    quantity = int(input("Enter quantity: "))
    price = float(input("Enter price: "))

    if category not in tax_rates or quantity <= 0 or price < 0:
        print("Invalid product details!")
        continue

    amount = quantity * price
    subtotal += amount

    products.append({
        "name": name,
        "category": category,
        "quantity": quantity,
        "price": price,
        "amount": amount
    })

# Discount calculation
if subtotal >= 10000:
    discount_percent = 15
elif subtotal >= 5000:
    discount_percent = 10
elif subtotal >= 2000:
    discount_percent = 5
else:
    discount_percent = 0

discount = subtotal * discount_percent / 100

# Maximum concession limit
max_discount = 2000
if discount > max_discount:
    discount = max_discount

# Calculate discount proportionally for each item
discount_ratio = discount / subtotal if subtotal > 0 else 0

# Calculate tax after discount
print("\n========== ITEMIZED BILL ==========")

for p in products:

    item_discount = p["amount"] * discount_ratio
    taxable_amount = p["amount"] - item_discount

    tax_rate = tax_rates[p["category"]]
    tax = taxable_amount * tax_rate / 100

    total_tax += tax

    print("\nProduct:", p["name"])
    print("Category:", p["category"])
    print("Quantity:", p["quantity"])
    print("Unit Price: Rs.", p["price"])
    print("Amount: Rs.", round(p["amount"], 2))
    print("Discount: Rs.", round(item_discount, 2))
    print("Tax: Rs.", round(tax, 2))

# Final bill
final_amount = subtotal - discount + total_tax

print("\n========== FINAL BILL ==========")
print("Subtotal: Rs.", round(subtotal, 2))
print("Discount: Rs.", round(discount, 2))
print("Total Tax: Rs.", round(total_tax, 2))
print("Maximum Discount Limit: Rs.", max_discount)
print("Final Payable Amount: Rs.", round(final_amount, 2))

print("\nThank you for shopping!")

