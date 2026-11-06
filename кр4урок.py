class Hero:
    def __init__(self, name: str, lvl: int, hp: int):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f"{self.name} готов к бою!")


class MageHero(Hero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int):
        super().__init__(name, lvl, hp)
        self.mp = mp

    def action(self):
        print(f"Маг {self.name} кастует заклинание! MP: {self.mp}")


class WarriorHero(MageHero):
    def __init__(self, name: str, lvl: int, hp: int, mp: int = 0):
        super().__init__(name, lvl, hp, mp)

    def action(self):
        print(f"Воин {self.name} рубит мечом! Уровень: {self.lvl}")


class BankAccount:
    bank_name = "Simba"

    def __init__(self, hero: Hero, balance: float, password: str):
        self.hero = hero
        self._balance = balance
        self.__password = password

    def login(self, password: str) -> bool:
        return self.__password == password

    @property
    def full_info(self) -> str:
        return f"Герой: {self.hero.name}, Баланс: {self._balance} SOM"

    @classmethod
    def get_bank_name(cls) -> str:
        return cls.bank_name

    def bonus_for_level(self) -> int:
        return self.hero.lvl * 10

    def __str__(self) -> str:
        return f"{self.hero.name} | Баланс: {self._balance} SOM"

    def __add__(self, other):
        if not isinstance(other, BankAccount):
            return NotImplemented
        if type(self.hero) is type(other.hero):
            return self._balance + other._balance
        else:
            return "Ошибка: Нельзя сложить счета героев разных классов!"

    def __eq__(self, other) -> bool:
        if not isinstance(other, BankAccount):
            return NotImplemented
        return type(self.hero) is type(other.hero) and self.hero.lvl == other.hero.lvl


if __name__ == "__main__":
    mage1 = MageHero("Merlin", 50, 100, 150)
    mage2 = MageHero("Gandalf", 50, 90, 200)
    warrior = WarriorHero("Conan", 50, 200)

    mage1.action()
    warrior.action()

    acc1 = BankAccount(mage1, 5000, "pass123")
    acc2 = BankAccount(mage2, 3000, "pass456")
    acc3 = BankAccount(warrior, 4000, "pass789")

    print(acc1)
    print(acc2)

    print("Банк:", acc1.get_bank_name())
    print("Бонус за уровень:", acc1.bonus_for_level(), "SOM")

    print("\n=== Проверка __add__ ===")
    print("Сумма счетов двух магов:", acc1 + acc2)
    print("Сумма мага и воина:", acc1 + acc3)

    print("\n=== Проверка __eq__ ===")
    print("Mage1 == Mage2 ?", acc1 == acc2)
    print("Mage1 == Warrior ?", acc1 == acc3)
