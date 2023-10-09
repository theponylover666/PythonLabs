import sys

sys.path.insert(1, 'c:\\Users\\diman\\Лабы\\PythonLabs\\Classes')

from person import Person


person1 = Person("Андрей", "Алексеев", 5)
person2 = Person("Павел", "Павлов", 3)
person3 = Person("Иван", "Иванов", 4)


print(person1.get_info())
print(person2.get_info())
print(person3.get_info())

weakest_person = min(person1, person2, person3, key=lambda x: x.qualification)

if weakest_person.qualification == person1.qualification:
    del weakest_person
    del person1
    input()
elif weakest_person.qualification == person2.qualification:
    del weakest_person
    del person2
    input()
else:
    del weakest_person
    del person3
    input()