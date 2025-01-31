from game.controller.dungeon_controller import DungeonController
from game.generator.character_generator import CharacterGenerator

DUNGEON_MAP = ["St", " ", "E", "E", " ", "E", "Ex"]

player_generator = CharacterGenerator("game/text_data/player_data.json", is_enemy=False)
enemy_generator = CharacterGenerator("game/text_data/enemy_data.json", is_enemy=True)

controller = DungeonController(DUNGEON_MAP, player_generator, enemy_generator)
controller.start_game()
