from game.entities.character import Character


class TestCharacter:
    def test_character_creation(self, player_generator, fix_camel_case_keys):
        data = player_generator.generate()
        data = fix_camel_case_keys(data)

        character = Character(**data)
        assert isinstance(
            character, Character
        ), "Character have to be an instance of Character class"
        assert (
            character.name == data["name"]
        ), f"{character.name} have to be equal to {data["name"]}"
        assert character.hp > 0, f"{character.hp} have to be greater then 0"

    def test_take_damage(
        self, player_generator, fix_camel_case_keys, convert_weapon_armor
    ):
        data = player_generator.generate()
        data = fix_camel_case_keys(data)
        data = convert_weapon_armor(data)

        character = Character(**data)
        default_hp = character.hp
        character.take_damage(3)
        assert (
            character.hp == default_hp - 1
        ), f"Character hp ({character.hp}) have to be {default_hp-1}"

    def test_is_alive(
        self, player_generator, fix_camel_case_keys, convert_weapon_armor
    ):
        data = player_generator.generate()
        data = fix_camel_case_keys(data)
        data = convert_weapon_armor(data)

        character = Character(**data)
        assert character.is_alive(), "Have to be alive as a default"
        character.take_damage(100)
        assert not character.is_alive(), "Character is alive"
