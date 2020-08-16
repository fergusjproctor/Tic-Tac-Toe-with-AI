prime_numbers = []
for a in range(2, 1001):
    if not any(a % n == 0 for n in range(2, a)):
        prime_numbers.append(a)
