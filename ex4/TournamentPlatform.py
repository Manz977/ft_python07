from typing import Dict
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self.cards: Dict[str, TournamentCard] = {}
        self.matches_played = 0

    def register_card(self, card: TournamentCard) -> str:
        self.cards[card.card_id] = card

        return (
            f"{card.name} (ID: {card.card_id}):\n"
            f"- Interfaces: [Card, Combatable, Rankable]\n"
            f"- Rating: {card.rating}\n"
            f"- Record: {card.wins}-{card.losses}"
        )

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        card1 = self.cards[card1_id]
        card2 = self.cards[card2_id]

        card1.update_wins(1)
        card1.rating += 16

        card2.update_losses(1)
        card2.rating -= 16

        self.matches_played += 1

        return {
            "winner": card1_id,
            "loser": card2_id,
            "winner_rating": card1.rating,
            "loser_rating": card2.rating
        }

    def get_leaderboard(self) -> list:
        sorted_cards = sorted(self.cards.values(), key=lambda c: c.rating,
                              reverse=True)
        leaderboard = []
        for index, card in enumerate(sorted_cards, start=1):
            leaderboard.append(f"{index}. {card.name}- Rating: "
                               f"{card.rating} ({card.wins}-{card.losses})")
        return leaderboard

    def generate_tournament_report(self) -> dict:
        total_cards = len(self.cards)

        if total_cards > 0:
            avg_rating = int(sum(c.rating for c in self.cards.values()) /
                             total_cards)
        else:
            avg_rating = 0

        return {
            "total_cards": total_cards,
            "matches_played": self.matches_played,
            "avg_rating": avg_rating,
            "platform_status": 'active'
        }
