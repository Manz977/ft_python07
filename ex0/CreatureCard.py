from ex0.Card import Card, Rarity


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, card_type: str,
                 attack: int, health: int):
        super().__init__(name, cost, rarity, card_type)
        if attack <= 0 or health <= 0:
            raise ValueError("Attack and Health must be a positive number")
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": "Creature summoned to battlefield"
        }

    def attack_target(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage_dealt": self.attack,
            "combat_resolved": True
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info.update({
            "type": self.card_type,
            "attack": self.attack,
            "health": self.health
        })
        return info
