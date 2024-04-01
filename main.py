# 1. Создайте базовый класс `Animal`, который будет содержать общие атрибуты (например, `name`, `age`) и методы (`make_sound()`, `eat()`)
# для всех животных.
# 2. Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`, которые наследуют от класса `Animal`.
# Добавьте специфические атрибуты и переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`, которая принимает список животных и вызывает метод `make_sound()`
# для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию о животных и сотрудниках. Должны быть методы для добавления
# животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут иметь специфические методы (например, `feed_animal()`
# для `ZooKeeper` и `heal_animal()` для `Veterinarian`).

class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("")

    def eat(self):
        print("оно кушает")

class Bird(Animal):
    def __init__(self, name, age, take_egg):
        self.name = name
        self.age = age
        self.take_egg = take_egg

class Mammal(Animal):
    def __init__(self, name, age, hear_cut):
        self.name = name
        self.age = age
        self.hear_cut = hear_cut

class Reptile(Animal):
    def __init__(self, name, age, clear_skin):
        self.name = name
        self.age = age
        self.clear_skin = clear_skin


straus = Bird("Коаткоцапль", 12, 2)
panda = Mammal("Линдзянь", 24, 12)
reptile = Reptile("Каа", 60, 6)



straus.eat()
