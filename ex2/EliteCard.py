from ex0.Card import Card, Rarity
from ex2.Combatable import Combatable
from ex2.Magical import Magical
from typing import List, Dict, Any
from enum import Enum
import random


class CombatType(Enum):
    MELEE = "melee"
    RANGED = "ranged"
    MAGIC = "magic"


class EliteCard(Card, Combatable, Magical):
    def __init__(self, name: str, cost: int, rarity: Rarity,
                 card_type: str, attack_power: int, defense_value: int,
                 mana_pool: int):
        super().__init__(name, cost, rarity, card_type)
        self.attack_power = attack_power
        self.defense_value = defense_value
        self.mana_pool = mana_pool

    def attack(self, target) -> dict:
        bouns_damage = random.randint(0, 4)
        total_damge = self.attack_power + bouns_damage
        return {
            "attacker": self.name,
            "target": target,
            "damage": total_damge,
            "combat_type": CombatType.MELEE.value
        }

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = max(0, incoming_damage - self.defense_value)
        damage_blocked = incoming_damage - damage_taken
        return {
            "defender": self.name,
            "damage_taken": damage_taken,
            "damage_blocked": damage_blocked,
            "still_alive": True
        }

    def get_combat_stats(self) -> dict:
        return {
            "Current attack power": self.attack_power,
            "Current defense value": self.defense_value
        }

    def channel_mana(self, amount: int) -> dict:
        self.mana_pool += amount
        return {
            "channeled": amount,
            "total_mana": self.mana_pool
        }

    def cast_spell(self, spell_name: str,
                   targets: List[str]) -> Dict[str, Any]:
        mana_cost = 4
        self.mana_pool -= mana_cost

        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": mana_cost
        }

    def get_magic_stats(self) -> dict:
        return {
            "mana_pool": self.mana_pool
        }

    def play(self, game_state: dict) -> dict:
        print(f"Playing {self.name} (Elite Card):\n")

        print("Combat phase:")

        combat_res = self.attack("Enemy")
        print(f"Attack result: {combat_res}")

        defense_res = self.defend(5)
        print(f"Defense result: {defense_res}")

        print("\nMagic phase:")
        magic_res = self.cast_spell("Fireball", ["Enemy1", "Enemy2"])
        print(f"Spell cast: {magic_res}")
        mana_results = self.channel_mana(3)
        print(f"Mana Channel: {mana_results}")
        return {
            "combat": combat_res,
            "defense": defense_res,
            "magic": magic_res
        }
