from ex0.Card import Rarity
from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main():
    print("\n=== DataDeck Tornument Platform ===\n")
    print("\nRegistering Tournament Cards...\n")

    tournament_platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, Rarity.RARE, "Creature",
                            "dragon_001", 1200)
    wizard = TournamentCard("Ice Wizard", 4, Rarity.RARE, "creature",
                            "wizard_001", 1150)

    print(tournament_platform.register_card(dragon))
    print()
    print(tournament_platform.register_card(wizard))

    print("\nCreating tournament match...")
    match_result = tournament_platform.create_match("dragon_001",
                                                    "wizard_001")
    print(f"Match result: {match_result}")

    print("\nTournament Leaderboard:")
    leaderboard = tournament_platform.get_leaderboard()
    for entry in leaderboard:
        print(entry)

    print(f"Platform Report: "
          f"{tournament_platform.generate_tournament_report()}\n")
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
