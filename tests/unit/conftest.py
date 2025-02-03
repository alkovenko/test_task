import json
from pathlib import Path

import pytest

from game.combat.autocombat import AutoCombat
from game.controller.dungeon_controller import DungeonController
from game.entities.armor import Armor
from game.entities.character import Character
from game.entities.weapon import Weapon
from game.generator.character_generator import CharacterGenerator


@pytest.fixture
def load_json():
    def _load(filename):
        json_path = (
            Path(__file__).parent.parent.parent / "game" / "text_data" / filename
        )
        with open(json_path, "r", encoding="utf-8") as f:
            return json.load(f)

    return _load


@pytest.fixture
def player_generator(mocker, load_json):
    player_data = load_json("player_data.json")

    mocker.patch.object(CharacterGenerator, "load_data", return_value=player_data)
    return CharacterGenerator("mocked_player_data.json", is_enemy=False)


@pytest.fixture
def enemy_generator(mocker, load_json):
    enemy_data = load_json("enemy_data.json")

    mocker.patch.object(CharacterGenerator, "load_data", return_value=enemy_data)
    return CharacterGenerator("mocked_enemy_data.json", is_enemy=True)


@pytest.fixture
def dungeon_controller(player_generator, enemy_generator):
    return DungeonController(["St", "E", "Ex"], player_generator, enemy_generator)


@pytest.fixture
def combat(
    player_generator, enemy_generator, fix_camel_case_keys, convert_weapon_armor
):
    player_data = player_generator.generate()
    enemy_data = enemy_generator.generate()

    player_data = fix_camel_case_keys(player_data)
    enemy_data = fix_camel_case_keys(enemy_data)

    player_data = convert_weapon_armor(player_data)
    enemy_data = convert_weapon_armor(enemy_data)

    player = Character(**player_data)
    enemy = Character(**enemy_data)

    return AutoCombat(player, enemy)


@pytest.fixture
def fix_camel_case_keys():
    def _fix_keys(data):
        data["death_description"] = data.pop("deathDescription", None)
        data["weapon"]["hit_probability"] = data["weapon"].pop("hitProbability", None)
        return data

    return _fix_keys


@pytest.fixture
def convert_weapon_armor():
    def _convert(data):
        data["weapon"] = Weapon.from_dict(data["weapon"])
        data["armor"] = Armor.from_dict(data["armor"])
        return data

    return _convert
