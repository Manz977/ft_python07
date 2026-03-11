from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 card_type: str, card_id: str, rating: int):
        super().__init__(name, cost, rarity, card_type)
        self.card_id = card_id
        self.rating = rating

        self.wins = 0
        self.losses = 0

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.wins += wins

    def update_losses(self, losses: int) -> None:
        self.losses += losses

    def get_rank_info(self) -> dict:
        return {
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def play(self, game_state: dict) -> dict:
        return {"action: ": f"{self.name} enters the tournament!"}

    def attack(self, target) -> dict:
        return {"action": f"{self.name} attacks {target}!"}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - 1)
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": incoming_damage - damage_taken
        }

    def get_combat_stats(self) -> dict:
        return {
            "attack_power": 3,
            "defense_value": 1,
            "tournament_rating": self.rating
        }

    def get_tournament_stats(self) -> dict:
        return {
            "name": self.name,
            "id": self.card_id,
            "rating": self.rating,
            "record": f"{self.wins}-{self.losses}"
        }
