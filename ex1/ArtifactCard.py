from ex0.Card import Card, Rarity


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 durability: int, effect: str):
        super().__init__(name, cost, rarity, "Artifact")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def activate_ability(self) -> dict:
        self.durability -= 1
        return {
            "card_played": self.name,
            "effect": self.effect,
            "Durability": self.durability
        }
