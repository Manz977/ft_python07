from ex0.CreatureCard import CreatureCard
from ex0.Card import Rarity
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, EffectType
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Builder ===\n")

    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY,
                               "Creature", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, Rarity.RARE,
                            EffectType.DAMAGE,
                            "Deal 3 damage to target"))
    deck.add_card(ArtifactCard("Mana Crystal", 2, Rarity.COMMON, 3,
                               "Premanent: +1 mana per turn"))

    print(f"Deck stats: {deck.get_deck_stats()}\n")

    print("Drawing and playing cards:\n")
    for _ in range(3):
        card = deck.draw_card()
        if card:
            print(f"Drew: {card.name} ({card.card_type})")
            print(f"Play result: {card.play({})}\n")

    print("\nPolymorphism in action: Same interface, " +
          "different card behaviors!")


if __name__ == "__main__":
    main()
