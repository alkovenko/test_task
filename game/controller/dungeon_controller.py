from game.combat.autocombat import AutoCombat
from game.entities.armor import Armor
from game.entities.character import Character
from game.entities.weapon import Weapon
from game.generator.room_generator import RoomGenerator


class DungeonController:
    def __init__(self, dungeon_map, player_generator, enemy_generator):
        self.__dungeon = dungeon_map
        self.__position = 0
        self.__player = self.generate_character(player_generator)
        self.__room_generator = RoomGenerator("game/text_data/room_data.json")
        self.__enemy_generator = enemy_generator
        self.__game_running = True
        self.__room_descriptions = {}
        self.__room_enemies = {}

    def generate_character(self, generator):
        data = generator.generate()
        return Character(
            name=data["name"],
            hp=data["hp"],
            description=data["description"],
            death_description=data["deathDescription"],
            weapon=Weapon.from_dict(data["weapon"]),
            armor=Armor.from_dict(data["armor"]),
        )

    def describe_room(self):
        if self.__position not in self.__room_descriptions:
            self.__room_descriptions[self.__position] = (
                self.__room_generator.generate()["roomDescription"]
            )

        print(f"\n{self.__room_descriptions[self.__position]}")

        if self.__dungeon[self.__position] == "E":
            if self.__position not in self.__room_enemies:
                self.__room_enemies[self.__position] = self.generate_character(
                    self.__enemy_generator
                )

            enemy = self.__room_enemies[self.__position]
            if enemy.is_alive():
                print(f"В этой комнате {enemy.name}: {enemy.description}")
            else:
                print(f"Вы видите тело {enemy.name}, павшего в бою.")
        else:
            self.__room_enemies[self.__position] = None

    def move_forward(self):
        self.__position += 1
        print("Вы двигаетесь вперед...")
        self.describe_room()

    def move_backward(self):
        self.__position -= 1
        print("Вы возвращаетесь назад...")
        self.describe_room()

    def attack_enemy(self):
        enemy = self.__room_enemies.get(self.__position)

        if enemy and enemy.is_alive():
            combat = AutoCombat(self.__player, enemy)
            combat.combat()

            if not enemy.is_alive():
                print(f"Вы победили {enemy.name}! {enemy.death_description}")

            if not self.__player.is_alive():
                print(f"Вы погибли! {self.__player.death_description}")
                self.__game_running = False

    def exit_dungeon(self):
        print("Вы выбрались из подземелья! Поздравляем!")
        self.__game_running = False

    def get_available_actions(self):
        actions = {}

        enemy = self.__room_enemies.get(self.__position)
        enemy_alive = enemy and enemy.is_alive()

        if self.__position < len(self.__dungeon) - 1 and not enemy_alive:
            actions["1"] = "Пойти дальше"
        if self.__position > 0:
            actions["2"] = "Вернуться назад"
        if enemy_alive:
            actions["3"] = "Атаковать"
        if self.__dungeon[self.__position] == "Ex":
            actions["4"] = "Выйти из подземелья"
        actions["5"] = "Выйти из игры"

        return actions

    def start_game(self):
        print("Добро пожаловать в подземелье!")
        print(f"Вы - {self.__player.name}. {self.__player.description}")
        self.describe_room()

        while self.__game_running:
            actions = self.get_available_actions()

            if not actions:
                print("Нет доступных действий. Игра завершена.")
                self.__game_running = False
                break

            print("\nВыберите действие:")
            for key, action in actions.items():
                print(f"{key}. {action}")

            choice = input("> ")

            if choice in actions:
                if choice == "1":
                    self.move_forward()
                elif choice == "2":
                    self.move_backward()
                elif choice == "3":
                    self.attack_enemy()
                elif choice == "4":
                    self.exit_dungeon()
                elif choice == "5":
                    print("Выход из игры...")
                    self.__game_running = False
            else:
                print("Неверный ввод, попробуйте снова.")
