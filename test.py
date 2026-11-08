name = "Amnat Aonjaroen"
age = 21
score = 70
is_student = True

for i in range(100):
    print(i+1)

if (is_student):
    status = "เป็นนักศึกษา"
else:
    status = "ไม่เป็นนักศึกษา"

if (score >= 80):
    grade = "A"
elif (score >=70 and score < 80):
    grade = "B"
elif (score >=60 and score < 70):
    grade = "C"
elif (score >=50 and score < 60):
    grade = "D"
elif (score < 50):
    grade = "F"



num1 = int(input("ตัวเลข 1 : "))
num2 = int(input("ตัวเลข 2 : "))

print(f"จำนวนบวก {num1 + num2}")
print(f"จำนวนลบ {num1 - num2}")
print(f"จำนวนคูณ {num1 * num2}")
print(f"จำนวนหาร {num1 / num2:.2f}")

print(f"\n ชื่อ {name} อายุ {age} คะแนน {score} สถานะ {status} เกรด : {grade}")


