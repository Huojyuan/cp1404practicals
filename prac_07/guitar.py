"""Guitar class for storing details about guitars and checking their age."""

from datetime import datetime

# Set CURRENT_YEAR using system date or fixed year if preferred
CURRENT_YEAR = datetime.now().year
VINTAGE_AGE = 50


class Guitar:
    """Represents a guitar with a name, year of manufacture, and cost."""

    def __init__(self, name='', year=0, cost=0):
        """
        Initialize a Guitar instance.

        :param name: str, the name of the guitar
        :param year: int, the year the guitar was made
        :param cost: float, the cost of the guitar
        """
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """
        Return a nicely formatted string representation of the guitar.

        :return: str, formatted as "Name (Year) : $Cost"
        """
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """
        Get the age of the guitar in years.

        :return: int, how many years old the guitar is
        """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """
        Determine if the guitar is vintage (50 years or older).

        :return: bool, True if vintage, else False
        """
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Enable sorting by comparing years (older guitars come first)."""
        return self.year < other.year
