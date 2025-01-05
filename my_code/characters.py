class Player:

    def __init__(self, name, hp, dmg):
        self.name = name
        self.hp = hp
        self.dmg = dmg

    def change_hp(self, new_hp):
        self.hp = new_hp

    def change_dmg(self, new_dmg):
        self.dmg = new_dmg