from abc import ABC, abstractmethod

class Hero(ABC):
    def __init__(self, name: str, level: int, health: int, strength: int):
        self.name = name
        self.level = level
        self.__health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def rest(self):
        print(f"{self.name} отдыхает")
        self.__health += 1

    @abstractmethod
    def attack(self):
        pass

class Warrior(Hero):
    def attack(self):
        print(f"{self.name} атакует мечом")

class Mage(Hero):
    def attack(self):
        print(f"{self.name} использует магию")

class Assassin(Hero):
    def attack(self):
        print(f"{self.name} атакует из-под тишка")

if __name__ == "__main__":
    warrior = Warrior("Конан", 5, 100, 15)
    mage = Mage("Гэндальф", 8, 60, 5)
    assassin = Assassin("Эцио", 6, 80, 12)

    heroes = [warrior, mage, assassin]

    for hero in heroes:
        hero.greet()
        hero.attack()
        hero.rest()
