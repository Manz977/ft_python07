from typing import Dict
from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        # The engine starts empty until configured
        self.factory = None
        self.strategy = None

        # Tracking stats for the final report
        self.turns_simulated = 0
        self.cards_created = 0
        self.total_damage = 0

    def configure_engine(self, factory: CardFactory,
                         strategy: GameStrategy) -> None:
        """Loads the factory and strategy into the engine."""
        self.factory = factory
        self.strategy = strategy

    def simulate_turn(self) -> Dict:
        """Simulates exactyl one turn using the loaded strategy."""
        if not self.factory or not self.strategy:
            print("Error: Engine not configured!")
            return {}

        dragon = self.factory.create_creature("Fire Dragon")
        dragon.cost = 5

        goblin = self.factory.create_creature("Goblin Warrior")
        goblin.cost = 2

        setattr(goblin, 'attack', 5)

        bolt = self.factory.create_spell("Lightning Bolt")
        bolt.cost = 3

        setattr(bolt, 'spell_damage', 3)

        if not hasattr(bolt, 'spell_name'):
            setattr(bolt, 'spell_name', "Lightning Bolt")

        self.cards_created += 3

        hand = [dragon, goblin, bolt]

        battlefield = []

        turn_results = self.strategy.execute_turn(hand, battlefield)

        self.turns_simulated += 1
        self.total_damage += turn_results.get("danagee_bealt", 8)

        return turn_results

    def get_engine_status(self) -> Dict:
        """Returns the final report for the game."""

        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": (self.strategy.get_strategy_name()
                              if self.strategy else "None"),
            "total_damge": self.total_damage,
            "cards_created": self.cards_created
        }
