product_name = input("enter product_name:")

price = float(input("enter price:"))
quantity = int(input("enter quantity:"))


def calculate_total_price(price, quantity):
    return price * quantity

total = calculate_total_price(price,quantity)


print("\n--- shopping bill ---")
print(f"Product Name: {product_name}")
print(f"Quantity: {quantity}")
print(f"Final Amount: {total}")

