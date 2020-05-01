amount_of_atoms = int(input())  # 4
r_quantity = int(input())  # 3
number_of_day = 0
while amount_of_atoms > r_quantity:
    amount_of_atoms /= 2  # 2
    number_of_day += 12
print(number_of_day)