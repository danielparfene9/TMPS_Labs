import json

def save_game(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

def load_game(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def random_chance(chance):
    from random import randint
    return randint(1, 100) <= chance
