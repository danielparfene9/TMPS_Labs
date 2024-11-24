import json

class Player:
    def __init__(self, hp=100, hunger=50, thirst=50, money=20, inventory=None):
        self.hp = hp
        self.hunger = hunger
        self.thirst = thirst
        self.money = money
        self.inventory = inventory or []

    def update_stat(self, stat, value):
        if hasattr(self, stat):
            setattr(self, stat, max(0, getattr(self, stat) + value))

    def add_item(self, item):
        self.inventory.append(item)

    def save(self, filepath):
        with open(filepath, 'w') as f:
            json.dump(self.__dict__, f)

    @classmethod
    def load(cls, filepath):
        with open(filepath, 'r') as f:
            data = json.load(f)
        return cls(**data)
