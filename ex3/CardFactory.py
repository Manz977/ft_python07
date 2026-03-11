from abc import ABC, abstractmethod
from typing import Dict, Union
from ex0.Card import Card


class CardFactory(ABC):

    @abstractmethod
    def create_creature(self, name_or_power: Union[str, int, None] = None
                        ) -> Card:
        """Creates a creature card."""
        pass

    @abstractmethod
    def create_spell(self, name_or_power: Union[str, int, None] = None
                     ) -> Card:
        """Creates a spell card."""
        pass

    @abstractmethod
    def create_artifact(self, name_or_power: Union[str, int, None] = None
                        ) -> Card:
        """Creates an artifact card."""
        pass

    @abstractmethod
    def create_themed_deck(self, size: int) -> Dict:
        """Generates a full deck of random cards."""
        pass

    @abstractmethod
    def get_supported_types(self) -> Dict:
        """Returns a dictionary of types this factory can build."""
        pass
