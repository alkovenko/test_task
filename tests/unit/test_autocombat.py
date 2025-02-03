class TestAutoCombat:
    def test_combat(self, combat):
        combat.combat()
        assert (
            not combat.enemy.is_alive() or not combat.player.is_alive()
        ), "Enemy or player have to be dead after combat"
