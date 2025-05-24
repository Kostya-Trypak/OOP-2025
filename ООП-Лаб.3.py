import copy

# Клас Користувач
class User:
    def __init__(self, name, role, permissions):
        self.name = name
        self.role = role
        self.permissions = permissions  # список прав

    def display_info(self):
        print(f"Ім'я: {self.name}")
        print(f"Роль: {self.role}")
        print(f"Права доступу: {', '.join(self.permissions)}")

    def clone(self):
        # Глибока копія — важливо, бо список permissions має бути незалежним
        return copy.deepcopy(self)

# Демонстрація патерна Prototype
def main():
    # Створюємо прототип адміністратора
    admin_prototype = User("ADMIN_TEMPLATE", "Admin", ["read", "write", "delete"])

    # Копіюємо його для нового користувача
    user1 = admin_prototype.clone()
    user1.name = "Іван"

    # Створимо ще одного користувача, теж копіюючи шаблон
    user2 = admin_prototype.clone()
    user2.name = "Олена"
    user2.permissions.remove("delete")  # обмежимо права

    print("Користувач 1:")
    user1.display_info()

    print("\nКористувач 2:")
    user2.display_info()

    print("\nОригінальний шаблон (адмін):")
    admin_prototype.display_info()

if __name__ == "__main__":
    main()
