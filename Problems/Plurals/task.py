number = int(input())
word = input()

# write a condition for plurals
if number == 1:
    print(f"{number} {word}")
if number > 1 or number == 0:
    print(f"{number} {word}s")
