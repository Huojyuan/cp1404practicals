from guitar import Guitar

FILENAME = "guitars.csv"


def main():
    """Main program to load, display, sort, add, and save guitars."""
    guitars = load_guitars(FILENAME)

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nGuitars sorted by year:")
    display_guitars(guitars)

    guitars += add_new_guitars()

    save_guitars(FILENAME, guitars)
    print(f"\nGuitars saved to {FILENAME}")


def load_guitars(filename):
    """Read guitars from a CSV file into a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        for line in file:
            name, year, cost = line.strip().split(',')
            guitars.append(Guitar(name, int(year), float(cost)))
    return guitars


def display_guitars(guitars):
    """Display a list of guitars."""
    for i, guitar in enumerate(guitars, start=1):
        print(f"Guitar {i}: {guitar}")


def add_new_guitars():
    """Prompt user to add new guitars and return them as a list."""
    print("\nAdd new guitars (enter blank name to finish):")
    new_guitars = []
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: "))
            new_guitars.append(Guitar(name, year, cost))
        except ValueError:
            print("Invalid input. Please enter a valid year and cost.")
    return new_guitars


def save_guitars(filename, guitars):
    """Write the list of guitars to the CSV file."""
    with open(filename, 'w') as file:
        for guitar in guitars:
            file.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")


if __name__ == "__main__":
    main()
