from typing import List, Dict
from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: List) -> List:
        sorted_targets = []

        if "Enemy Player" in available_targets:
            sorted_targets.append("Enemy Player")

        for target in available_targets:
            if target != "Enemy Player":
                sorted_targets.append(target)
        return sorted_targets

    def execute_turn(self, hand: List, battelfield: List) -> Dict:
        try:
            hand.sort(key=lambda card: getattr(card, 'cost', 99))
        except Exception as e:
            print(f"Could not sort hand: {e}")

        cards_played = []
        mana_used = 0
        damage_dealt = 0
        max_mana = 5

        for card in hand:
            card_cost = getattr(card, 'cost', 1)

            if mana_used + card_cost <= max_mana:
                card_name = getattr(card, 'name', getattr(card,
                                                          'spell_name',
                                                          'Unknown Card'))
                cards_played.append(card_name)
                mana_used += card_cost

                if hasattr(card, 'attack'):
                    damage_dealt += card.attack

                elif card_name == "Lightning Bolt":
                    damage_dealt += 3
                elif hasattr(card, "effect_type"):
                    damage_dealt += 2

        targets = self.prioritize_targets(["Enemy Creature",
                                           "Enemy Player"])

        return {
            "cards_played": cards_played,
            "mana_used": mana_used,
            "targets_attacked": [targets[0]] if targets else [],
            "damage_dealt": damage_dealt
        }
