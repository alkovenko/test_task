import random

from game.generator.base_generator import BaseGenerator


class RoomGenerator(BaseGenerator):

    def generate(self):
        room_description = random.choice(self.data["rooms"])

        generated_room = {
            "isEnemyPresent": random.choice([True, False]),
            "roomDescription": room_description,
        }

        return generated_room
