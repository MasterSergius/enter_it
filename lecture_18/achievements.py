class Achievements:
    DAMAGE_ACHIEVEMENT = 1000
    HEAL_ACHIEVEMENT = 100

    def __init__(self):
        self.damage_achievement = False
        self.heal_achievement = False
        self._total_dmg = 0
        self._total_heal = 0
        # ...
        # 100

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

    def track_damage_achievement(self, damage):
        # check if we got achievement
        self._total_dmg += damage
        if self._total_dmg >= achievements.DAMAGE_ACHIEVEMENT:
            achievements.register_damage_achievement()

    def track_heal_achievement(self, heal):
        # check if we got achievement
        self._total_heal += heal
        if self._total_heal >= achievements.HEAL_ACHIEVEMENT:
            achievements.register_heal_achievement()

    def register_damage_achievement(self):
        self.damage_achievement = True

    def register_heal_achievement(self):
        self.heal_achievement = True


achievements = Achievements()


def track_attack_achievement(attack_func):
    def tracking_wrapper(self, enemy):
        attack_func(self, enemy)
        achievements.track_attack_achievement(self.damage)

    return tracking_wrapper


def track_heal_achievement(heal_func):
    def tracking_wrapper(self, heal_hp):
        heal_func(self, heal_hp)
        achievements.track_heal_achievement(heal_hp)

    return tracking_wrapper
