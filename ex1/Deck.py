import random
from typing import List
from ex0.Card import Card


class Deck:
    def __init__(self) -> None:
        self.cards: List[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def draw_card(self) -> Card:
        if not self.cards:
            raise ValueError("List of cards is empty")
        return self.cards.pop()

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def remove_card(self, card_name: str) -> bool:
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        if total_cards == 0:
            return {
                "total_cards": 0,
                "creatures": 0,
                "spells": 0,
                "artifacts": 0,
                "avg_cost": 0.0
            }
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0
        for card in self.cards:
            total_cost += card.cost
            if card.card_type == "Creature":
                creatures += 1
            elif card.card_type == "Spell":
                spells += 1
            elif card.card_type == "Artifact":
                artifacts += 1

        avg_cost = int((total_cost / total_cards) + 0.5)

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost
        }
