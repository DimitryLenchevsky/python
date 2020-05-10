
def start_menu():
    print("\t1. Выход \n\
    2. Добавить контакт \n\
    3. Заменить контакт \n")
    choice = int(input("\tВаш выбор: \n"))
    choose(choice)

def choose(choice):
    if choice == 1:
        exit()
    elif choice == 2 or 3:
        key = input("Введите ФИО: ")
        weight = int(input("Введите массу тела в килограммах: "))
        height = int(input("Введите Ваш рост в сантиметрах: "))
        sex = input("Введите Ваш пол: ")
        age = int(input("Введите Ваш возраст: "))
        value = [weight, height, sex, age]
        person[key] = value
        bmi = weight / (height * height / 10000)
        recomendation(bmi)
        conclusion_person()
    else:
            print("Упс, что-то пошло не так")
    
def conclusion_person():
    for key, value in person.items():
        print(key, ",", value)

def recomendation(bmi):
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

def main():
    while True:
        start_menu()





person = {}
main()
