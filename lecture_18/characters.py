import logging

from achievements import track_attack_achievement
from achievements import track_heal_achievement


class Character:
    BASE_HP = 100
    BASE_DMG = 5
    BASE_DEFENCE = 0

    def __init__(self):
        self._max_hp = self.BASE_HP
        self._hp = self.BASE_HP
        self.damage = self.BASE_DMG
        self.defence = self.BASE_DEFENCE

    def take_damage(self, dmg: int):
        clean_damage = dmg - self.defence
        if clean_damage > 0:
            self._hp -= clean_damage
        return clean_damage

    @track_attack_achievement
    def attack(self, enemy):
        enemy.take_damage(self.damage)

    @track_heal_achievement
    def heal(self, heal_hp: int):
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp

        logging.info(f"Heal for {heal_hp} hp")

    def make_turn(self):
        logging.info(f"Character {self.__class__} makes turn")


class Warrior(Character):
    BASE_HP = 150
    BASE_DMG = 10


class Ranger(Character):
    pass


class Wizard(Character):
    BASE_HP = 80
    BASE_DMG = 2


class Berserk(Warrior):
    def take_damage(self, dmg: int):
        damage = super().take_damage(dmg)
        if damage > 0:
            self.damage += 1
        logging.info(f"Taken damage {damage}")


# SOLID, L - Liskov Substitution Principle, D - Dependency Inversion Principle
# Dependency Injection
class Priest(Wizard):
    pass


class Sorcerer(Wizard):
    def weapon_powerup(self):
        print(f"{self.__class__} powered up weapon")


class Warlock(Wizard):
    def weapon_powerup(self):
        print(f"{self.__class__} powered up weapon")
