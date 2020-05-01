# put your python code here
sum_of_numbers = 0
numbers_list = []
sum_of_square = 0
user_input = int(input())
if user_input != 0:
    while True:
        sum_of_numbers += user_input
        numbers_list.append(user_input)
        user_input = int(input().strip())
        if sum_of_numbers == 0:
            for number in numbers_list:
                sum_of_square += (number * number)
            break
else:
    sum_of_square = user_input
print(sum_of_square)