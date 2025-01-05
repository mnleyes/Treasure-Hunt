from my_code.items import books

# classes

class Player:

    def __init__(self, playername):
        self.name = playername

class Room:
    def __init__(self, items):
        self.exit_open = False
        self.items = [items]

class startingRoom(Room):
    def __init__(self):
        super().__init__()
        self.exit_open = False

class bookRoom(Room):
    pass

class outside:

# game

print("Welcome to Treasure Hunt!")

playername = input("Player Name: ")
player = Player(playername)

print("""
      Your eyes are bleary.
      You find yourself in a damp, cobbled room.
      You came here to find treasure.
      """)

