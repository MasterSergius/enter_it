import logging

logging.basicConfig(format="%(message)s", level=logging.DEBUG)


class Achievements:
    DAMAGE_ACHIEVEMENT = 1000
    HEAL_ACHIEVEMENT = 100

    def __init__(self):
        self.damage_achievement = False
        self.heal_achievement = False

    def print_achievements(self):
        print("Achievements\n")
        print(
            f"Demolisher (Total damage >= {self.DAMAGE_ACHIEVEMENT} dmg): {
                self.damage_achievement
            }"
        )
        print(
            f"Healer (Total heal >= {self.HEAL_ACHIEVEMENT} hp): {
                self.heal_achievement
            }"
        )

    def register_damage_achievement(self):
        self.damage_achievement = True

    def register_heal_achievement(self):
        self.heal_achievement = True


class Character:
    BASE_HP = 100
    BASE_DMG = 5

    def __init__(self):
        self._max_hp = self.BASE_HP
        self._hp = self.BASE_HP
        self.damage = self.BASE_DMG
        self._total_damage = 0
        self._total_heal = 0
        self.achievements = Achievements()

    def take_damage(self, dmg: int):
        pass

    def attack(self):
        # attack logic goes here
        # TBD

        # check if we got achievement
        self._total_dmg += self.damage
        if self._total_dmg >= self.achievements.DAMAGE_ACHIEVEMENT:
            self.achievements.register_damage_achievement()

        logging.info(f"Did damage for {self.damage} hp\n")

    def heal(self, heal_hp: int):
        # heal
        self._hp += heal_hp
        if self._hp > self._max_hp:
            self._hp = self._max_hp

        # check if we got achievement
        self._total_heal += heal_hp
        if self._total_heal >= self.achievements.HEAL_ACHIEVEMENT:
            self.achievements.register_heal_achievement()

        logging.info(f"Healed for {heal_hp} hp\n")


class Warrior(Character):
    BASE_HP = 150
    BASE_DMG = 10


class Ranger(Character): ...


class Wizard(Character):
    BASE_HP = 80
    BASE_DMG = 2


warrior = Warrior()
warrior.heal(10)
warrior.heal(90)
warrior.achievements.print_achievements()
