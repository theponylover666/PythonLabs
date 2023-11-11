import math
from matplotlib import pyplot as plt
from prettytable import PrettyTable


# Сама функция
def function(x):
    # Проверка на то, какое число ввел пользователь
    if x <= 0:
        return 'Не существует'
    else:
        return math.log(x)


def main():
    # Ввод и проверка на отсутвие ошибок
    try:
        a = float(input("Введите начало диапазона a\n"))
    except:
        print("Ошибка: Переменная " + '\033[31ma\033[0m' + " должна быть числом")
        return
    try:
        b = float(input("Введите конец диапазона b\n"))
    except:
        print("Ошибка: Переменная " + '\033[31mb\033[0m' + " должна быть числом")
        return
    try:
        h = float(input("Введите шаг h\n"))
    except:
        print("Ошибка: Переменная " + '\033[31mh\033[0m' + " должна быть числом")
        return
    th = ["№", "x", "f(x)"]
    td = []
    # Переменные для работы с функцией
    x = a
    i = 1
    x_values = []
    y_values = []
    # Вывод всех значений функции
    while x <= b:
        td += [i, x, function(x)]
        x_values += [float(x)]
        if function(x) != "Не существует":
            y_values += [float(function(x))]
        else:
            y_values += [0]
        i += 1
        x += h
    columns = len(th)
    table = PrettyTable(th)
    while td:
        table.add_row(td[:columns])
        td = td[columns:]

    print(table)

    # Построение графика
    plt.plot(x_values, y_values)
    plt.title('График')
    plt.xlabel('Значения оси x')
    plt.ylabel('Значения оси y')
    plt.show()


# main function
if __name__ == '__main__':
    main()
