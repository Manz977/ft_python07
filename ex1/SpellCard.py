from ex0.Card import Card, Rarity
from enum import Enum


class EffectType(Enum):
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    def __init__(self, spell_name: str, cost: int, rarity: Rarity,
                 effect_type: EffectType, effect: str):
        super().__init__(spell_name, cost, rarity, "Spell")
        self.effect_type = effect_type
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.effect
        }

    def resolve_effect(self, targets: list) -> dict:
        return {
            "spell_name": self.name,
            "effect_type": self.effect_type.value,
            "targets_affected": targets,
            "status": "Resolved"
        }
