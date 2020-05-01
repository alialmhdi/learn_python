sum_of_number = 0
count = 0
while True:
    user_input = input()
    if user_input == ".":
        break
    sum_of_number += int(user_input)
    count += 1
print(sum_of_number / count)
