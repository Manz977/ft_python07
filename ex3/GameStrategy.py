from abc import ABC, abstractmethod
from typing import List, Dict


class GameStrategy(ABC):

    @abstractmethod
    def execute_turn(self, hand: List, battelfield: List) -> Dict:
        """Executes a turn based on the specific strategy."""
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """Returns the name of the strategy."""
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: List) -> List:
        """Orders targets based on the strategy's priority."""
        pass
