import pytest


class TestEndToEnd:
    @pytest.mark.parametrize(
        "game_setup, mock_user_input",
        [(["St", " ", " ", "Ex"], ["1", "1", "1", "4"])],
        indirect=True,
    )
    def test_full_dungeon(self, game_setup, mock_user_input, capfd):
        game_setup.start_game()
        captured = capfd.readouterr()
        assert not game_setup._DungeonController__game_running, "Game is still running"
        assert (
            "Вы выбрались из подземелья! Поздравляем!" in captured.out
        ), "Message expected after finishing the game"

    @pytest.mark.parametrize(
        "game_setup, mock_user_input",
        [
            (
                ["St", "E", "E", "E", "E", "E", "E"],
                ["1", "3", "1", "3", "1", "3", "1", "3", "1", "3", "1", "3"],
            )
        ],
        indirect=True,
    )
    def test_game_over_by_death(self, game_setup, mock_user_input, capfd):
        game_setup.start_game()
        captured = capfd.readouterr()
        assert (
            not game_setup._DungeonController__player.is_alive()
        ), "Player have to be dead"
        assert "Вы погибли!" in captured.out, "Message expected after death"

    @pytest.mark.parametrize(
        "game_setup, mock_user_input",
        [(["St", " ", " ", "Ex"], ["1", "2", "1", "1", "1", "5"])],
        indirect=True,
    )
    def test_backward_movement(self, game_setup, mock_user_input):
        game_setup.start_game()
        assert not game_setup._DungeonController__game_running, "Game is still running"

    @pytest.mark.parametrize(
        "game_setup, mock_user_input",
        [(["St", "E", "E", "Ex"], ["abc", "1", "999", "-1", "5"])],
        indirect=True,
    )
    def test_invalid_input(self, game_setup, mock_user_input, capfd):
        game_setup.start_game()
        captured = capfd.readouterr()
        assert not game_setup._DungeonController__game_running, "Game is still running"
        assert (
            "Неверный ввод, попробуйте снова." in captured.out
        ), "Message expected after invalid input"

    @pytest.mark.parametrize(
        "game_setup, mock_user_input",
        [(["St"], ["1", "5"])],
        indirect=True,
    )
    def test_start_message(self, game_setup, mock_user_input, capfd):
        game_setup.start_game()
        captured = capfd.readouterr()
        assert "Добро пожаловать в подземелье!" in captured.out
