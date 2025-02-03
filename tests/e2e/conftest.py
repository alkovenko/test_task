import json
from pathlib import Path

import pytest

from game.controller.dungeon_controller import DungeonController
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
def game_setup(request, player_generator, enemy_generator):
    dungeon_map = request.param
    return DungeonController(dungeon_map, player_generator, enemy_generator)


@pytest.fixture
def mock_user_input(monkeypatch, request):
    user_inputs = iter(request.param)
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))
