import random
from enum import Enum
from typing import Union

from ex3.CardFactory import CardFactory
from ex0.Card import Card, Rarity
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard, EffectType


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: Rarity, card_type: str):
        super().__init__(name, cost, rarity, card_type)

    def play(self, game_state: dict) -> dict:
        return {"action": f"Activated artifact {self.name}"}


class CardCategory(Enum):
    CREATURE = "Creature"
    SPELL = "Spell"
    ARTIFACT = "Artifact"


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        # 1. Matched exactly to your expected output
        self.supported = {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"]
        }

    # 2. THE MISSING PIECE: Extensible Card Type Registration
    def register_card_type(self, category: str, card_name: str) -> None:
        """Dynamically adds new card types to the factory's capabilities."""
        if category in self.supported:
            if card_name not in self.supported[category]:
                self.supported[category].append(card_name)
        else:
            self.supported[category] = [card_name]

    def create_creature(self, name_or_power: Union[str, int, None] = None
                        ) -> Card:
        try:
            if isinstance(name_or_power, int):
                name = f"Creature Level {name_or_power}"
            elif isinstance(name_or_power, str):
                name = name_or_power
            else:
                name = random.choice(self.supported["creatures"]).title()

            return CreatureCard(
                name=name,
                cost=random.randint(1, 5),
                rarity=Rarity.COMMON,
                card_type=CardCategory.CREATURE.value,
                attack=random.randint(1, 5),
                health=random.randint(1, 5)
            )
        except Exception as e:
            print(f"Error creating creature: {e}")
            return CreatureCard("Default Goblin", 1, Rarity.COMMON,
                                CardCategory.CREATURE.value, 2, 1)

    def create_spell(self, name_or_power: Union[str, int, None] = None
                     ) -> Card:
        try:
            if isinstance(name_or_power, str):
                name = name_or_power
            elif isinstance(name_or_power, int):
                name = f"Spell Level {name_or_power}"
            else:
                # Capitalize the spell name (e.g., "Fireball")
                name = random.choice(self.supported["spells"]).title()

            # Using your exact SpellCard signature!
            return SpellCard(
                spell_name=name,
                cost=random.randint(2, 6),
                rarity=Rarity.RARE,
                effect_type=EffectType.DAMAGE,
                effect=f"Deals {random.randint(3, 8)} magical damage."
            )
        except Exception as e:
            print(f"Error creating spell: {e}")
            # Fallback must also match your exact signature
            return SpellCard(
                spell_name="Default Fireball",
                cost=3,
                rarity=Rarity.COMMON,
                effect_type=EffectType.DAMAGE,
                effect="Deals 3 damage."
            )

    def create_artifact(self, name_or_power: Union[str, int, None] = None
                        ) -> Card:
        try:
            if isinstance(name_or_power, str):
                name = name_or_power
            elif isinstance(name_or_power, int):
                name = f"Artifact Level {name_or_power}"
            else:
                name = (random.choice(self.supported["artifacts"])
                        .replace("_", " ").title())

            return ArtifactCard(
                name=name,
                cost=random.randint(0, 4),
                rarity=Rarity.RARE,
                card_type=CardCategory.ARTIFACT.value
            )
        except Exception as e:
            print(f"Error creating artifact: {e}")
            return ArtifactCard("Default Ring", 2, Rarity.COMMON,
                                CardCategory.ARTIFACT.value)

    def create_themed_deck(self, size: int) -> dict:
        deck = []
        for _ in range(size):
            choice = random.choice(["creatures", "spells", "artifacts"])
            if choice == "creatures":
                deck.append(self.create_creature())
            elif choice == "spells":
                deck.append(self.create_spell())
            else:
                deck.append(self.create_artifact())

        return {
            "deck_size": size,
            "cards": [card.name for card in deck]
        }

    def get_supported_types(self) -> dict:
        return self.supported
