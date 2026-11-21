import random
from collections import Counter

DICE_ART = {
    1: (
        "+-------+",
        "|       |",
        "|   o   |",
        "|       |",
        "+-------+",
    ),
    2: (
        "+-------+",
        "| o     |",
        "|       |",
        "|     o |",
        "+-------+",
    ),
    3: (
        "+-------+",
        "| o     |",
        "|   o   |",
        "|     o |",
        "+-------+",
    ),
    4: (
        "+-------+",
        "| o   o |",
        "|       |",
        "| o   o |",
        "+-------+",
    ),
    5: (
        "+-------+",
        "| o   o |",
        "|   o   |",
        "| o   o |",
        "+-------+",
    ),
    6: (
        "+-------+",
        "| o   o |",
        "| o   o |",
        "| o   o |",
        "+-------+",
    ),
}


def print_dice_side_by_side(values):
    """Displays rolled dice faces horizontally using ASCII art."""
    for row in range(5):
        print("  ".join(DICE_ART[val][row] for val in values))


def roll_dice(num_dice=1, sides=6):
    """Rolls 'num_dice' dice each having 'sides' faces and returns the list of results."""
    return [random.randint(1, sides) for _ in range(num_dice)]


def run_simulation(trials, num_dice=2):
    """Simulates rolling dice 'trials' times and displays frequency & probability stats."""
    totals = [sum(roll_dice(num_dice, 6)) for _ in range(trials)]
    counts = Counter(totals)
    min_sum = num_dice
    max_sum = num_dice * 6

    print(f"\n--- Simulation Results ({trials:,} rolls of {num_dice} dice) ---")
    print(f"{'Sum':<6} {'Count':<10} {'Probability':<13} {'Distribution'}")
    print("-" * 55)
    for outcome in range(min_sum, max_sum + 1):
        freq = counts[outcome]
        prob = (freq / trials) * 100
        bar = "#" * int(prob * 1.5)
        print(f"{outcome:<6} {freq:<10} {prob:>6.2f}%       {bar}")


def main():
    history = []

    while True:
        print("\n=== Dice Simulator (random module) ===")
        print("1. Roll a Single 6-Sided Die")
        print("2. Roll Multiple 6-Sided Dice")
        print("3. Run Probability Simulation (N Trials)")
        print("4. View Roll History")
        print("0. Exit")

        choice = input("Enter your choice (0-4): ").strip()
        if choice == "1":
            result = roll_dice(1, 6)
            history.append(result)
            print(f"\nYou rolled: {result[0]}")
            print_dice_side_by_side(result)
        elif choice == "2":
            try:
                count = int(input("How many dice to roll (1-6)? ").strip())
                if not 1 <= count <= 6:
                    raise ValueError
                results = roll_dice(count, 6)
                history.append(results)
                print(f"\nRolled {count} dice -> Values: {results} | Total Sum: {sum(results)}")
                print_dice_side_by_side(results)
            except ValueError:
                print("Please enter a valid number between 1 and 6.")
        elif choice == "3":
            try:
                trials = int(input("Enter number of simulation rolls (e.g., 1000): ").strip())
                num_dice = int(input("Enter number of dice per roll (1 or 2): ").strip())
                if trials <= 0 or num_dice not in (1, 2):
                    raise ValueError
                run_simulation(trials, num_dice)
            except ValueError:
                print("Enter positive trials and 1 or 2 dice.")
        elif choice == "4":
            print("\n--- Roll History ---")
            if not history:
                print("No rolls recorded yet.")
            else:
                for idx, roll in enumerate(history, start=1):
                    print(f"Roll {idx}: {roll} (Sum = {sum(roll)})")
        elif choice == "0":
            print("Exiting Dice Simulator.")
            break
        else:
            print("Invalid choice. Please enter 0-4.")


if __name__ == "__main__":
    main()