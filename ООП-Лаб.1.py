from abc import ABC, abstractmethod


# Наслідування: Абстрактний базовий клас
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self._name = name  # Інкапсуляція: закритий атрибут
        self._age = age  # Інкапсуляція: закритий атрибут

    @abstractmethod
    def make_sound(self):
        pass

    def info(self):
        return f"Name: {self._name}, Age: {self._age}"

# Похідний клас "Dog"
class Dog(Animal):
    def __init__(self, name: str, age: int, breed: str):
        super().__init__(name, age)
        self._breed = breed  # Інкапсуляція

    def make_sound(self):
        return "Вууф!"

    def get_breed(self):
        return self._breed

# Похідний клас "Cat"
class Cat(Animal):
    def __init__(self, name: str, age: int, color: str):
        super().__init__(name, age)
        self._color = color  # Інкапсуляція

    def make_sound(self):
        return "Мяу!"

    def get_color(self):
        return self._color

# Поліморфізм: створення колекції об'єктів
animals = [
    Dog("Джейк", 3, "Лабрадор"),
    Cat("Мурчик", 2, "Чорний"),
    Dog("Лейла", 5, "Бульдог")
]

# Виклик абстрактного методу make_sound для всіх об'єктів
for animal in animals:
    print(f"{animal.info()} - Sound: {animal.make_sound()}")