# put your python code here
while True:
    user_input = int(input().strip())
    while user_input < 10:
        user_input = int(input().strip())
    if user_input > 100:
        break
    print(user_input)