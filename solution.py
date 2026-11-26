# Case Study 7: Retail Billing with Multiple Discount Rules

def create_invoice(products):
    """products: list of (name, category, unit_price, quantity) tuples."""
    tax_rates = {"grocery": 0.05, "other": 0.12}
    subtotal = 0
    tax_total = 0
    lines = []

    for product in products:
        name, category, price, quantity = product  # tuple unpacking
        if price < 0 or quantity <= 0:
            raise ValueError("Price cannot be negative and quantity must be positive.")
        category = category.lower()
        if category not in tax_rates:
            raise ValueError("Category must be 'grocery' or 'other'.")

        amount = price * quantity
        tax = amount * tax_rates[category]
        subtotal += amount
        tax_total += tax
        lines.append((name, quantity, price, amount, tax))

    discount = min(subtotal * 0.10, 500) if subtotal >= 2000 else 0
    payable = subtotal + tax_total - discount
    return lines, subtotal, tax_total, discount, payable


def main():
    products = [
        ("Rice", "grocery", 650, 2),
        ("Notebook", "other", 80, 5),
        ("Cooking Oil", "grocery", 180, 3),
    ]
    lines, subtotal, tax, discount, payable = create_invoice(products)

    print("RETAIL INVOICE")
    print("-" * 62)
    print(f"{'Product':18} {'Qty':>4} {'Price':>9} {'Amount':>10} {'Tax':>8}")
    for name, qty, price, amount, item_tax in lines:
        print(f"{name:18} {qty:>4} {price:>9.2f} {amount:>10.2f} {item_tax:>8.2f}")
    print("-" * 62)
    print(f"Subtotal:       Rs. {subtotal:.2f}")
    print(f"Tax total:      Rs. {tax:.2f}")
    print(f"Discount:       Rs. {discount:.2f}")
    print(f"Amount payable: Rs. {payable:.2f}")


if __name__ == "__main__":
    main()
