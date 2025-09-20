def calculate_total(price: float, quantity: int, apply_discount: bool) -> float:

    total = price * quantity

    if apply_discount:
        total = total * 0.9  # Apply 10% discount

    return total
