import os.path
import random
import this


# Создаем функцию для сортировки пузырьком
def bubble_sort(arr):
    # Цикл for перебирает все элементы списка
    for i in range(len(arr)):
        # Вложенный цикл for перебирает все элементы списка, кроме последнего
        for j in range(len(arr) - 1):
            # Если текущий элемент больше следующего, то меняем их местами
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# Создаем функцию для генерации случайного списка
def random_array(a,b,c):
    # Создаем пустой список
    arr = []
    # Цикл for добавляет в список a случайных чисел в диапазоне от b до c
    for i in range(a):
        arr.append(random.randint(b, c))
    return arr

# Создаем функцию для чтения данных из файла
def read_file(a):
    file_name = a + ".txt"
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    # Открываем файл с именем a и режимом чтения
    file = open(file_path, "r")
    # Считываем данные из файла и сохраняем их в переменную data
    data = file.read()
    # Закрываем файл
    file.close()
    # Преобразуем данные из строки в список
    array = eval(data)
    # Вызываем функцию convert_to_list для преобразования списка в список списков
    arr = convert_to_list(array)
    return arr

# Создаем функцию для записи данных в файл
def write_file(a, arr):
    file_name = a + ".txt"
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    # Открываем файл с именем a и режимом записи
    file = open(file_path, "w")
    # Преобразуем список в строку
    arr_str = str(arr)
    # Записываем строку в файл
    file.write(arr_str)
    # Закрываем файл
    file.close()

# Создаем функцию для преобразования списка в список списков
def convert_to_list(arr):
    # Создаем пустой список
    lst = []
    # Цикл for добавляет каждый элемент из списка arr в список lst
    for el in arr:
        lst.append(el)
    return lst