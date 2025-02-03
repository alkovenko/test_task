class Weapon:
    def __init__(self, name, description, damage, hit_probability):
        self.name = name
        self.description = description
        self.damage = damage
        self.hit_probability = hit_probability

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["name"],
            data["description"],
            data["damage"],
            data.get("hit_probability", data.get("hitProbability")),
        )
