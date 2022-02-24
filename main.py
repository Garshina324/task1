import random
import time


def task1():
    try:
        name = "Настя"
        print(f"Здравствуй, {name}")
    except ValueError:
        print("должно быть одно слово")
    return


def task2():
    age = 19
    name = "Настя"
    print(f"Привет, {name}.Тебе уже {age} лет!! Какая молодец!!!")
    return


def task3():
    name = "Настя "
    variant1 = name * 5
    variant2 = name + name + name + name + name
    print(f"Здесь вроде бы 2 одинаковые строки, но они получены разными способами:\n {variant1}\n {variant2}")
    return


def task4():
    name = input("Как тебя зовут? ")
    try:
        age = int(input("Сколько тебе лет? "))
        print(f"Привет, {name}. Твой возраст {age}")
    except ValueError:
        print("Это строка, а нужно число")
    return


def task5():
    name = input("Как тебя зовут? ")
    try:
        age = int(input("Сколько тебе лет? "))
        if 0 <= age <= 15:
            print(f"Привет, {name}")
            print("Ой ти мой маленький")
        elif 16 <= age <= 25:
            print(f"Привет, {name}")
            print("Свободная касса?")
        elif 26 <= age <= 35:
            print(f"Привет, {name}")
            print("Ты в полном расцвете сил, но спина уже побаливает")
        elif 36 <= age <= 50:
            print(f"Привет, {name}")
            print("Ты еще не старый(ая)... Повторяю.. Ты еще не старый(ая)!!!!")
        elif 51 <= age <= 100:
            print(f"Привет, {name}")
            print("Про почтенный возраст мы не шутим")
        else:
            print(f"Привет, {name}")
            print("А врать плохо")
    except ValueError:
        print("Это строка, а нужно число")
    return


def task6():
    name = input("Как тебя зовут? ")
    print(f"{name[2:(len(name) - 1)]}\n{name[(len(name) - 3):]}\n{name[:5]}\n{name[::-1]}")
    return


def task7():
    name = input("Как тебя зовут? ")
    try:
        age = int(input("Сколько тебе лет? "))

        sum = (age // 10) + (age % 10)
        pr = (age // 10) * (age % 10)
        print(
            f"Длина твоего имени: {len(name)}\nсумма чисел твоего возраста: {sum}\nпроизведение чисел твоего возраста {pr}")
    except ValueError:
        print("Это строка, а нужно число")
    return


def task8():
    name = input("Как тебя зовут? ")
    print(f"{name.upper()}\n{name.lower()}\n{name[:1].upper() + name[1:]}\n{name[:1].lower() + name[1:]}")
    return


def task10():
    try:
        answer = int(input("36 + 5*2 = "))
        if answer == 46:
            print("это правильный ответ")
        else:
            print("это неправильный ответ")
    except ValueError:
        print("Это строка, а нужно число")
    return


def surprise():
    variants_list = ["камень", "ножницы", "бумага"]
    coins = 10
    print("был введен секретный код")
    time.sleep(2)
    print(f"Приветствую в игре 'камень-ножницы-бумага'!!\nНачальное количество монет: {coins}")
    while True:
        try:
            user_choice = int(input("1)камень 2)ножницы 3)бумага 4)выход\n "))
            if coins == 0 or user_choice == 4:
                print("игра закончена")
                break
            computer_choice = random.choice(variants_list)
            print(f"компьютер: {computer_choice}")
            match user_choice:
                case 1:
                    if computer_choice == "ножницы":
                        coins += 10
                        print("вы выиграли")
                    elif computer_choice == "бумага":
                        coins -= 5
                        print("вы проиграли")
                    else:
                        print("ничья")

                case 2:
                    if computer_choice == "ножницы":
                        print("ничья")

                    elif computer_choice == "бумага":
                        coins += 10
                        print("вы выиграли")
                    else:
                        coins -= 5
                        print("вы проиграли")

                case 3:
                    if computer_choice == "ножницы":
                        coins -= 5
                        print("вы проиграли")
                    elif computer_choice == "бумага":
                        print("ничья")
                    else:
                        coins += 10
                        print("вы выиграли")

            print(f"Ваше текущее количество монет: {coins}")

        except ValueError:
            print("Это строка, а нужно число")
    return


while True:
    num_of_function = input("Введите номер задания: ")
    if num_of_function == "0":
        print("Завершение цикла")
        break
    match num_of_function:
        case "1":
            task1()
        case "2":
            task2()
        case "3":
            task3()
        case "4":
            task4()
        case "5":
            task5()
        case "6":
            task6()
        case "7":
            task7()
        case "8":
            task8()
        case "10":
            task10()
        case "123":
            surprise()
