number = int(input().strip())
square = []
list_numbers = []
for i in range(number):
    list_numbers.append(int(input().strip()))
for x in list_numbers:
    if x % 7 == 0:
        print(x * x)
