from abc import ABC, abstractmethod


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str, card_type: str):
        self.name = name
        self.cost = cost
        self.rarity = rarity
        self.card_type = card_type

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> dict:
        return {
            "name": self.name,
            "cost": self.cost,
            "rarity": self.rarity
        }

    def is_playable(self, availabe_mana: int) -> bool:
        return self.cost <= availabe_mana
