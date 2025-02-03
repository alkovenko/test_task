class TestDungeonController:
    def test_move_forward(self, dungeon_controller):
        dungeon_controller.move_forward()
        assert (
            dungeon_controller._DungeonController__position == 1
        ), "Position have to be equal 1 after moving forward"

    def test_move_backward(self, dungeon_controller):
        dungeon_controller.move_forward()
        dungeon_controller.move_backward()
        assert (
            dungeon_controller._DungeonController__position == 0
        ), "Position have to be equal 0 after moving forward and backward"

    def test_attack_enemy(self, dungeon_controller):
        dungeon_controller.move_forward()
        dungeon_controller.attack_enemy()
        enemy = dungeon_controller._DungeonController__room_enemies[1]
        assert (
            not enemy.is_alive()
            or not dungeon_controller._DungeonController__player.is_alive()
        ), "Enemy or player have to be dead after combat"

    def test_exit_dungeon(self, dungeon_controller):
        dungeon_controller.move_forward()
        dungeon_controller.move_forward()
        dungeon_controller.exit_dungeon()
        assert (
            not dungeon_controller._DungeonController__game_running
        ), "Game is still running after exit"
