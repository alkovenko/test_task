from game.entities.weapon import Weapon


class TestWeapon:
    def test_weapon_creation(self, load_json, fix_camel_case_keys):
        player_data = load_json("player_data.json")
        player_data = fix_camel_case_keys(player_data)
        weapon_data = player_data["weapon"]
        weapon = Weapon(**weapon_data)
        assert (
            weapon.name == weapon_data["name"]
        ), f"{weapon.name} have to be equal to {weapon_data["name"]}"
        assert (
            weapon.damage == weapon_data["damage"]
        ), f"{weapon.damage} have to be equal to {weapon_data["damage"]}"
