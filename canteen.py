def calculate_total(price):
    discount = 0

    if price > 300:
        discount = price * 0.10

    total = price - discount
    total = total + total * 0.05

    return round(total, 2)
