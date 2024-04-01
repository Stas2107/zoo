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

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print("")

    def eat(self):
        print(f"{self.name} кушает")


class Bird(Animal):
    def __init__(self, name, age, take_egg):
        super().__init__(name, age)
        self.take_egg = take_egg

    def make_sound(self):
        print("А-А-А-А")


class Mammal(Animal):
    def __init__(self, name, age, hair_cut):
        super().__init__(name, age)
        self.hair_cut = hair_cut

    def make_sound(self):
        print("фух-ты фух-ты")


class Reptile(Animal):
    def __init__(self, name, age, clear_skin):
        super().__init__(name, age)
        self.clear_skin = clear_skin

    def make_sound(self):
        print("Пшшшш")


class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

    def work(self):
        print(f"{self.name}, {self.position}, на работе.")

    def feed_animal(self, any):
        print(f"{self.name} покормил {any}")

    def heal_animal(self, any):
        print(f"{self.name} полечил {any}")

class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)

    def add_employee(self, employee):
        self.employees.append(employee)

    def all_animals_sound(self):
        for animal in self.animals:
            animal.make_sound()


# Создание объектов
straus = Bird("Коаткоцапль", 12, 2)
panda = Mammal("Линдзянь", 24, 12)
reptile = Reptile("Каа", 60, 6)
zooKeeper = Employee("Дядя Ваня", "смотритель")
veterinarian = Employee("Тетя Нина", "ветеринар")

my_zoo = Zoo()
my_zoo.add_animal(straus)
my_zoo.add_animal(panda)
my_zoo.add_animal(reptile)
my_zoo.add_employee(zooKeeper)
my_zoo.add_employee(veterinarian)

# действия в зоопарке
my_zoo.all_animals_sound()
veterinarian.heal_animal(straus.name)
zooKeeper.feed_animal(panda.name)

# сохранить список фивотных и работников в файлы
with open("animals.txt", "w", encoding='utf-8') as animals:
    for animal in my_zoo.animals:
        animals.write(str(animal.name) + '\n')

with open("employers.txt", "w", encoding='utf-8') as employees:
    for employee in my_zoo.employees:
        employees.write(str(employee.name) + '\n')


