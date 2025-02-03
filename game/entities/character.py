import random


class Character:
    def __init__(self, name, hp, description, death_description, weapon, armor):
        self.name = name
        self.hp = hp
        self.description = description
        self.death_description = death_description
        self.weapon = weapon
        self.armor = armor

    def __str__(self):
        return f"{self.name} ({self.hp} HP)"

    def is_alive(self):
        return self.hp > 0

    def take_damage(self, damage):
        self.hp -= max(damage - self.armor.protection, 0)

    def attack(self, target):
        hit_chance = random.randint(0, 100)
        if hit_chance <= self.weapon.hit_probability:
            damage = self.weapon.damage
            target.take_damage(damage)
            return True, damage
        return False, 0
