
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
        conclusion_person()
    else:
            print("Упс, что-то пошло не так")
    
def conclusion_person():
    for key, value in person.items():
        print(key, ",", value)


person = {}
start_menu()
