from ex0.Card import Rarity
from ex2.EliteCard import EliteCard


def main() -> None:
    print("\n=== DataDeck Ability System ===\n")

    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']\n")

    arcane_warrior = EliteCard(
        "Arcane Warrior",
        5,
        Rarity.LEGENDARY,
        "Battlemage",
        5,
        3,
        8
    )
    arcane_warrior.play({})

    print("\nMultiple interface implementation successful!")


if __name__ == "__main__":
    main()
