class Person:
    # Создаем метод init для инициализации объекта при создании
    def __init__(self, name, surname, qualification=1):
        # Сохраняем значение атрибута name в переменную self.name
        self.name = name
        # Сохраняем значение атрибута surname в переменную self.surname
        self.surname = surname
        # Сохраняем значение атрибута qualification в переменную self.qualification, если оно не было передано при создании объекта, то по умолчанию равно 1
        self.qualification = qualification
    
    # Создаем метод get_info для получения информации об объекте
    def get_info(self):
        # Возвращаем строку с информацией об объекте, используя значения атрибутов self.name, self.surname и self.qualification
        return f"Имя: {self.name}\nФамилия: {self.surname}\nКвалификация: {self.qualification}"
    
    # Создаем метод del для прощания с объектом
    def __del__(self):
        # Выводим сообщение о прощании с объектом, используя значения атрибутов self.name и self.surname
        print(f"До свидания, мистер {self.name} {self.surname}")