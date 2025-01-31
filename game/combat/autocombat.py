class AutoCombat:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def attack_phase(self, attacker, defender):
        print(f"{attacker} атакует {defender}")
        hit, damage = attacker.attack(defender)
        if hit:
            print(f"{attacker.name} попал! Нанесено {damage} урона.")
            if not defender.is_alive():
                return True
        else:
            print(f"{attacker.name} промахнулся.")
        return False

    def combat(self):
        while self.player.is_alive() and self.enemy.is_alive():
            if self.attack_phase(self.player, self.enemy):
                break
            if self.attack_phase(self.enemy, self.player):
                break
