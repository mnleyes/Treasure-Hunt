
class Book:
    def __init__(self, name, benefit, description):
        self.name = name
        self.benefit = benefit
        self.description = description

bookHeal = Book("Healing Book", "Full Health", "A book that heals you.")
bookPower = Book("Strength Book", "Good Strength", "A book that gives you a lot of strength")
bookPuzzle1 = Book("??? Part 1", "?", "It's not clear what this does /n It is a part one.")
bookPuzzle2 = Book("??? Part 2", "?", "It's not clear what this does /n It is a part two.")

books = [bookHeal, bookPower, bookPuzzle1, bookPuzzle2]