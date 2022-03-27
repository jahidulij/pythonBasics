
class Person:
    def __init__(self, pName, pAge, pHeight):
        self.name = pName
        self.age = pAge
        self.height = pHeight

    def get_name(self):
        return f"Name: {self.name}"

    def set_name(self, newName):
        self.name = newName
    def get_person_info(self):
        return f"Name: {self.name}, Age: {self.age}, Height: {self.height}"

person_1 = Person("Kyle", "22", "5.7 feet")
person_2 = Person("James", "29", "6 feet")

print(person_1.get_name())
print(person_1.get_person_info())
print(person_1.set_name("Kyle Mills"))
print(person_1.get_person_info())