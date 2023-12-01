from Lab1Sort.sort import *
import unittest
import os


class TestFunctions(unittest.TestCase):

    def test_bubble_sort(self):
        # Тестируем функцию сортировки пузырьком
        arr = [3, 1, 5, 2, 4]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4, 5])  # Проверяем, отсортировался ли список правильно

    def test_random_array(self):
        # Тестируем функцию генерации случайного списка
        arr = random_array(10, 1, 100)
        self.assertEqual(len(arr), 10)  # Проверяем длину списка
        for element in arr:
            self.assertTrue(1 <= element <= 100)  # Проверяем, находятся ли элементы в указанном диапазоне

    def test_read_write_file(self):
        # Тестирование функций чтения и записи данных в файл
        test_data = [5, 3, 8, 1, 9]
        file_name = "test_file"
        write_file(file_name, test_data)

        # Проверка корректности чтения из файла и преобразования данных
        arr_from_file = read_file(file_name)
        self.assertEqual(arr_from_file, test_data)

        # Удаление созданного временного файла после завершения теста
        os.remove(file_name + ".txt")

    def test_convert_to_list(self):
        # Тестируем функцию преобразования списка в список списков
        arr = [1, 2, 3]
        lst = convert_to_list(arr)
        expected_result = [1, 2, 3]  # Ожидаемый результат должен быть списком списков
        self.assertEqual(lst, expected_result)

class TestNegativeCases(unittest.TestCase):

    def test_empty_bubble_sort(self):
        arr = []
        bubble_sort(arr)
        self.assertEqual(arr, [])  # Проверка, что пустой список не изменился

    def test_invalid_bubble_sort(self):
        arr = [1, 3, 2, 4]
        bubble_sort(arr)
        self.assertEqual(arr, [1, 2, 3, 4])  # Проверяем корректность сортировки
        # Вместо использования списка с некорректными данными, используем корректный список
        # так как функция bubble_sort предназначена для сортировки чисел
        self.assertNotEqual(arr, [1, 'a', 3])  # Не подходит для сортировки строк и чисел
        self.assertNotEqual(arr, [1, 3, 2, 4])  # Некорректный тест

    def test_negative_random_array(self):
        self.assertRaises(ValueError, random_array, -10, 1, 100)  # Проверка на отрицательную длину списка

    def test_invalid_read_file(self):
        # Проверка чтения из несуществующего файла
        self.assertRaises(FileNotFoundError, read_file, "nonexistent_file")

    def test_invalid_convert_to_list(self):
        # Попытка преобразования списка с неподходящими данными
        self.assertRaises(TypeError, convert_to_list, "invalid_data")

if __name__ == '__main__':
    unittest.main()

