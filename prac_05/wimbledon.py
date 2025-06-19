"""
Wimbledon Data Processor
Estimated time: 30 minutes
Actual time: 28 minutes

This program reads 'wimbledon.csv' and displays:
1. Champions and the number of times each has won.
2. Countries of champions in alphabetical order.

It uses a list of lists, a dictionary, and a set.
"""

FILENAME = "wimbledon.csv"

def load_wimbledon_data(filename):
    """Load data from the CSV file into a list of records."""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        next(in_file)  # Skip header
        records = [line.strip().split(",") for line in in_file]
    return records


def count_champions(data):
    """Count how many times each player has won."""
    champion_to_count = {}
    for record in data:
        champion = record[2]
        champion_to_count[champion] = champion_to_count.get(champion, 0) + 1
    return champion_to_count


def get_unique_countries(data):
    """Get a sorted set of unique countries."""
    countries = {record[1] for record in data}
    return sorted(countries)


def main():
    data = load_wimbledon_data(FILENAME)

    champions = count_champions(data)
    countries = get_unique_countries(data)

    print("Wimbledon Champions:")
    for champion, wins in sorted(champions.items()):
        print(f"{champion:20} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


if __name__ == "__main__":
    main()
