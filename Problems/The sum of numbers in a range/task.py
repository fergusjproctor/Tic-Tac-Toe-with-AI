def range_sum(numbers, start, end):
    total = 0
    for number in numbers:
        if start <= number <= end:
            total += number
    return total


input_numbers = [int(x) for x in input().split()]
a, b = input().split()
a = int(a)
b = int(b)
print(range_sum(input_numbers, a, b))
