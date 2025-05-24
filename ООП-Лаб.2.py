import math

# Принцип єдиної відповідальності: кожен клас описує лише одну фігуру
class Shape:
    def area(self):
        raise NotImplementedError("Метод area() має бути реалізований у підкласі")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Клас, який відповідає лише за виведення результатів
class AreaPrinter:
    def print_area(self, shape: Shape):
        print(f"Площа: {shape.area():.2f}")

# Демонстрація використання
def main():
    print("Оберіть фігуру:")
    print("1. Коло")
    print("2. Прямокутник")
    choice = input("Ваш вибір: ")

    printer = AreaPrinter()

    if choice == "1":
        radius = float(input("Введіть радіус: "))
        shape = Circle(radius)
    elif choice == "2":
        width = float(input("Введіть ширину: "))
        height = float(input("Введіть висоту: "))
        shape = Rectangle(width, height)
    else:
        print("Невірний вибір.")
        return

    printer.print_area(shape)

if __name__ == "__main__":
    main()
