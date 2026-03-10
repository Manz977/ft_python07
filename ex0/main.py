from ex0.Card import Rarity


try:
    from ex0.CreatureCard import CreatureCard
except ImportError as e:
    print(f"Error importing CreatureCard: {e}")
    exit(1)


def main() -> None:

    print("\n=== DataDeck Card Fundation ===\n")

    print("Testing Abstract Base Class Design:\n")
    print("CreatureCard Info:")

    try:
        card = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY,
                            "Creature", 7, 5)
        print(card.get_card_info())
    except ValueError as e:
        print(f"Error creating CreatureCard: {e}")
        return
    print()

    mana = 6
    print(f"Playing Fire Daragon with {mana} available:")
    try:
        print(f"Playable: {card.is_playable(mana)}")
        print(f"Play result: {card.play({})}\n")
    except Exception as e:
        print(f"Error during card play: {e}\n")

    print("Fire Dragon attacks Goblin Warrior:")
    try:
        print(f"Attack result: {card.attack_target('Goblin Warrior')}")
    except Exception as e:
        print(f"Error during attack: {e}")
    print()

    mana_test = 3
    print("Testing insufficient mana (3 available):")
    try:
        print(f"Playable: {card.is_playable(mana_test)}\n")
        print("Abstract pattern successfully demonstrated!")
    except Exception as e:
        print(f"Error during mana test: {e}")


if __name__ == "__main__":
    main()
