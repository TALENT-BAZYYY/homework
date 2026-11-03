import random

class Hero:
    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        print(f"Привет, я {self.name}, мой уровень {self.level}")

    def attack(self):
        print(f"{self.name} наносит удар!")
        self.strength -= 1

    def rest(self):
        print(f"{self.name} отдыхает…")
        self.health += 1


class Warrior(Hero):
    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        print(f"{self.name} (Воин) атакует мечом!")


class Mage(Hero):
    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        print(f"{self.name} (Маг) кастует заклинание!")


class Assassin(Hero):
    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        print(f"{self.name} (Ассасин) атакует из-под тишка!")


warrior_obj = Warrior("Конан", 10, 150, 20, 100)
mage_obj = Mage("Гэндальф", 12, 90, 8, 200)
assassin_obj = Assassin("Эцио", 11, 110, 15, 85)

heroes_dict = {
    "Warrior": warrior_obj,
    "Mage": mage_obj,
    "Assassin": assassin_obj
}

print("Выберите героя: Warrior / Mage / Assassin")
user_choice = input("Ваш выбор: ").strip()

if user_choice not in heroes_dict:
    print("Неверный выбор героя!")
else:
    player = heroes_dict[user_choice]
    
    ai_choice = random.choice(list(heroes_dict.keys()))
    enemy = heroes_dict[ai_choice]

    print(f"\nВы выбрали: {user_choice}")
    player.attack()
    
    print(f"Противник: {ai_choice}")
    enemy.attack()
    print("-" * 30)

    if user_choice == ai_choice:
        print("Ничья!")
    elif (user_choice == "Warrior" and ai_choice == "Assassin") or \
         (user_choice == "Assassin" and ai_choice == "Mage") or \
         (user_choice == "Mage" and ai_choice == "Warrior"):
        print(f"{user_choice} победил!")
    else:
        print(f"{ai_choice} победил!")
