mount = int(input())
sum_of_deposit = 50_000 <= mount <= 700_000
year = 0
balance = 0
while mount <= 700_000:
    mount = mount * 1.071
    year += 1
print(year)