import random

from game.generator.base_generator import BaseGenerator


class CharacterGenerator(BaseGenerator):
    def __init__(self, json_file, is_enemy):
        super().__init__(json_file)
        self.is_enemy = is_enemy

    def generate(self):
        if self.is_enemy:
            char_data = random.choice(self.data["enemies"])
        else:
            char_data = {
                "name": random.choice(self.data["names"]),
                "description": random.choice(self.data["descriptions"]),
                "deathDescription": random.choice(self.data["deathDescriptions"]),
                "hp": self.data["hp"],
            }

        weapon = (
            random.choice(self.data["weapons"])
            if self.is_enemy
            else self.data["weapon"]
        )
        armor = (
            random.choice(self.data["armors"]) if self.is_enemy else self.data["armor"]
        )

        return {
            "name": char_data["name"],
            "hp": char_data["hp"],
            "description": char_data["description"],
            "deathDescription": char_data["deathDescription"],
            "weapon": {
                "name": weapon["name"],
                "description": weapon["description"],
                "damage": weapon["damage"],
                "hitProbability": weapon["hitProbability"],
            },
            "armor": {
                "name": armor["name"],
                "description": armor["description"],
                "protection": armor["protection"],
            },
        }
