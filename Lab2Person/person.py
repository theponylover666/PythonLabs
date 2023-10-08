class Person:
    def __init__(self, name, surname, qualification=1):
        self.name = name
        self.surname = surname
        self.qualification = qualification
    
    def get_info(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\nКвалификация: {self.qualification}"
    
    def __del__(self):
        print(f"До свидания, мистер {self.name} {self.surname}")