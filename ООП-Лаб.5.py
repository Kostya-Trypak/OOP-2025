from abc import ABC, abstractmethod

# STRATEGY PATTERN
class MoveStrategy(ABC):
    @abstractmethod
    def move(self):
        pass

class WalkStrategy(MoveStrategy):
    def move(self):
        return "Йде пішки"

class WheelsStrategy(MoveStrategy):
    def move(self):
        return "Їде на колесах"

class FlyStrategy(MoveStrategy):
    def move(self):
        return "Летить"

# STATE PATTERN
class State(ABC):
    @abstractmethod
    def handle(self, robot):
        pass

class NormalState(State):
    def handle(self, robot):
        print("[Нормальний стан] Робот працює повноцінно.")
        print("Рух: " + robot.move_strategy.move())

class DamagedState(State):
    def handle(self, robot):
        print("[Пошкоджений стан] Робот обмежений у русі.")
        print("Рух: Йде повільно і обережно.")

class PowerSavingState(State):
    def handle(self, robot):
        print("[Енергозбереження] Робот мінімізує активність.")
        print("Рух: Лише за потреби.")

# CONTEXT
class Robot:
    def __init__(self, move_strategy: MoveStrategy, state: State):
        self.move_strategy = move_strategy
        self.state = state

    def set_move_strategy(self, strategy: MoveStrategy):
        self.move_strategy = strategy

    def set_state(self, state: State):
        self.state = state

    def act(self):
        self.state.handle(self)

# DEMO
def main():
    robot = Robot(WalkStrategy(), NormalState())

    while True:
        print("\n=== Керування роботом ===")
        print("1. Змінити стратегію руху")
        print("2. Змінити стан робота")
        print("3. Виконати дію")
        print("4. Вийти")

        choice = input("Ваш вибір: ")

        if choice == "1":
            print("Виберіть стратегію:")
            print("1. Йти пішки")
            print("2. Їхати на колесах")
            print("3. Летіти")
            strat_choice = input("-> ")
            if strat_choice == "1":
                robot.set_move_strategy(WalkStrategy())
            elif strat_choice == "2":
                robot.set_move_strategy(WheelsStrategy())
            elif strat_choice == "3":
                robot.set_move_strategy(FlyStrategy())
        elif choice == "2":
            print("Виберіть стан:")
            print("1. Нормальний")
            print("2. Пошкоджений")
            print("3. Енергозбереження")
            state_choice = input("-> ")
            if state_choice == "1":
                robot.set_state(NormalState())
            elif state_choice == "2":
                robot.set_state(DamagedState())
            elif state_choice == "3":
                robot.set_state(PowerSavingState())
        elif choice == "3":
            robot.act()
        elif choice == "4":
            print("Вихід...")
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
