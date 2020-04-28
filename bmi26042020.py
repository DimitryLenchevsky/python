weight = int(input("Давайте узнаем Ваш индекс массы тела. Введите массу тела в килограммах: "))
height = int(input("Введите Ваш рост в сантиметрах: "))
bmi = weight / (height * height / 10000)
print("Индекс Вашей массы тела равен: ", bmi)
if bmi <= 16:
    print("Выраженный дефицит массы тела")
elif bmi <= 18.5:
    print("Недостаточная (дефицит) масса тела")
elif bmi <= 25:
    print("Ваш индекс массы тела в норме")
elif bmi <= 30:
    print("Избыточная масса тела (предожирение)")
elif bmi <= 35:
    print("Ожирение")
elif bmi <= 40:
    print("Ожирение резкое")
elif bmi > 40:
    print("Очень резкое ожирение")

pass

tick = "|"
first = bmi - 10
second = 50 - bmi

scale = '10' + "=" * int(first) + tick + "=" * int(second) + "50"
print(scale)
