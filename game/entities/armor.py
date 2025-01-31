class Armor:
    def __init__(self, name, description, protection):
        self.name = name
        self.description = description
        self.protection = protection

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["description"], data["protection"])
