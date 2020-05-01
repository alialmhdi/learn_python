user_input = int(input().strip())
if user_input < 1:
    print("no army")
elif 1 <= user_input <= 9:
    print("few")
elif 10 <= user_input <= 49:
    print("pack")
elif 50 <= user_input <= 499:
    print("horde")
elif 500 <= user_input <= 999:
    print("swarm")
else:
    print("legion")