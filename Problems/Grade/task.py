student_grad = float(input())
max_score = float(input())
fun = student_grad * 100 / max_score
if 90 <= fun <= 100:
    print("A")
elif 80 <= fun < 90:
    print("B")
elif 70 <= fun < 80:
    print("C")
elif 60 <= fun < 70:
    print("D")
else:
    print("F")