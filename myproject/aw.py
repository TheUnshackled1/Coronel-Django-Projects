items = {
    "001": {"name": "Rolex", "price": 2500.0},
    "002": {"name": "Adidas", "price": 1500.0},
    "003": {"name": "Regatta", "price": 1500.0},
    "004": {"name": "Levis", "price": 800.0},
    "005": {"name": "BlueD", "price": 1000.0},
}

print("===== WELCOME TO POS SYSTEM! 🥰🥰🥰 =====")
print("AVAILABLE ITEMS:")

for code, details in items.items():
    print(f"Code: {code} - Name: {details['name'].capitalize()}, Price: PHP {details['price']:.2f}")

def print_receipt(cart, total_cost):
    print("\nReceipt")
    for item_code, quantity in cart.items():
        item = items[item_code]
        print(f"{item['name'].capitalize()} x{quantity} @ P{item['price']:.2f} = P{item['price'] * quantity:.2f}")
    print(f"Total cost: P{total_cost:.2f}")

def main():
    cart = {}
    total_cost = 0.0
    while True:
        item_code = input("Enter a 3-digit item code to add to cart (or 'done' to finish): ").strip()
        if item_code.lower() == "done":
            break
        elif item_code in items:
            quantity = int(input(f"Enter quantity for {items[item_code]['name']}: "))
            if item_code in cart:
                cart[item_code] += quantity
            else:
                cart[item_code] = quantity
            total_cost += items[item_code]["price"] * quantity
        else:
            print("Invalid item code. Please try again.⚠️⚠️⚠️⚠️")
    
    print_receipt(cart, total_cost)
    
    while True:
        cash_amount = float(input("Enter cash amount: P"))
        if cash_amount >= total_cost:
            change = cash_amount - total_cost
            print(f"Change: P{change:.2f}")
            print("Thank you for shopping🥰🥰\nCome again!🙋‍♂️🙋‍♂️🙋‍♂️")
            break
        else:
            print("Cash amount must be greater than or equal to the total cost. Please enter a valid amount.😱😱😱😱")

if __name__ == "__main__":
    main()
