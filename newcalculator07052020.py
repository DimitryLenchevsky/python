while True:

    first_name = input("Здравствтуйте. Что бы остановить программу, введите q. Для того что бы продолжить ведите ваше имя: ")
    if first_name == "q":
        break
    else:
        last_name = input("Введите Вашу фамилию: ")
        middle_name = input("Введите ваше отчество: ")
        weight = int(input("Введите массу тела в килограммах: "))
        height = int(input("Введите Ваш рост в сантиметрах: "))
        sex = input("Введите Ваш пол: ")
        age = int(input("Введите Ваш возраст: "))

        bmi = weight / (height * height / 10000)

        print("Индекс Вашей массы тела равен: ", bmi)
        if bmi <= 16:                                    
            print("Выраженный дефицит массы тела, больше кушайте!")
        elif bmi <= 18.5:
            print("Недостаточная (дефицит) масса тела. Больше кушайте!")
        elif bmi <= 25:
            print("Ваш индекс массы тела в норме")
        elif bmi <= 30:
            print("Избыточная масса тела (предожирение), постарайтесь больше двигаться!")
        elif bmi <= 35:
            print("Ожирение, постарайтесь больше двигаться и меньше есть!")
        elif bmi <= 40:
            print("Ожирение резкое, срочно сходите к врачу!")
        elif bmi > 40:
            print("Очень резкое ожирение, срочно сходите к врачу!")
        pass

        persons = {}
        info = [last_name, first_name, middle_name, weight, height, age, bmi, sex]

        persons['Фамилия'] = info[0]
        persons['Имя'] = info[1]
        persons['Отчество'] = info[2]
        persons['Масса в кг'] = info[3]
        persons['Рост'] = info[4]
        persons['Возраст'] = info[5]
        persons['bmi'] = info[6]
        persons['Пол'] = info[7]

        print(persons)

        # Вывод шкалы
        tick = "|"
        first = bmi - 10
        second = 50 - bmi

        scale = '10' + "=" * int(first) + tick + "=" * int(second) + "50"
        print(scale)