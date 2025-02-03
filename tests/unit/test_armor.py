from game.entities.armor import Armor


class TestArmor:
    def test_armor_creation(self, load_json):
        player_data = load_json("player_data.json")
        armor_data = player_data["armor"]
        armor = Armor(**armor_data)
        assert (
            armor.name == armor_data["name"]
        ), f"{armor.name} have to be equal to {armor_data["name"]}"
        assert (
            armor.protection == armor_data["protection"]
        ), f"{armor.protection} have to be equal to {armor_data["protection"]}"
