numbers = [int(x) for x in input().split()]
total = 0
for number in numbers:
    total += number
print(total / len(numbers))