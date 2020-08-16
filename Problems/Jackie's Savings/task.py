def final_deposit_amount(*interest, amount=1000):
    for monthly_interest in interest:
        amount = amount * (1 + monthly_interest / 100)
    return round(amount, 2)

