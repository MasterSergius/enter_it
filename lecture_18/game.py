import logging
import random


from characters import Character
from characters import Warrior
from characters import Ranger
from characters import Wizard


logging.basicConfig(format="%(message)s", level=logging.DEBUG)


class GameManager:
    def __init__(self, player: Character):
        self.player = player
        self.enemies = [random.choice((Warrior, Ranger, Wizard))() for i in range(10)]

    def player_turn(self):
        self.player.make_turn()

    def enemies_turn(self):
        for enemy in self.enemies:
            enemy.make_turn()


def main():
    # player choose Character
    player = Warrior()
    game_manager = GameManager(player)
    game_manager.player_turn()
    game_manager.enemies_turn()


if __name__ == "__main__":
    main()
