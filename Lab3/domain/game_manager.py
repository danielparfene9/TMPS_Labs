import json
from client.player import Player
from domain.command import *
from domain.strategy import *

class GameManager:
    def __init__(self, player_file='data/player.json', story_file='data/story_state.json'):
        try:
            self.player = Player.load(player_file)
        except Exception as e:
            self.player = Player()
        self.story_file = story_file
        self.current_chapter = None

    def load_story(self):
        with open(self.story_file, 'r') as f:
            self.story_data = json.load(f)

    def start_game(self):
        self.load_story()
        print("Welcome to The Whispering Wasteland!")
        self.play_chapter("Chapter 1")

    def play_chapter(self, chapter_name):
        self.current_chapter = self.story_data[chapter_name]
        print(f"--- {self.current_chapter['title']} ---")
        print(self.current_chapter['description'])
        print(f"\nStats: HP={self.player.hp}, Hunger={self.player.hunger}, Thirst={self.player.thirst}, Money={self.player.money}")
        print(f"Inventory: {self.player.inventory}")

        for idx, choice in enumerate(self.current_chapter['choices'], 1):
            print(f"{idx}. {choice['text']}")

        while True:
            try:
                choice_idx = int(input("Choose an option: ")) - 1
                if 0 <= choice_idx < len(self.current_chapter['choices']):
                    break
                else:
                    print("Invalid choice. Try again.")
            except ValueError:
                print("Please enter a valid number.")

        result = self.execute_choice(self.current_chapter['choices'][choice_idx])
        if result.get("next_chapter"):
            self.play_chapter(result["next_chapter"])

    def execute_choice(self, choice):
        print(choice['result']['description'])

        if 'command' in choice['result']:
            command_data = choice['result']['command']
            command = None

            if command_data['type'] == 'search':
                command = SearchCommand(command_data['items_found'])
            elif command_data['type'] == 'trade':
                command = TradeCommand(command_data['item'], command_data.get('price', 0))
            elif command_data['type'] == 'combat':
                
                combat_type = command_data['combat_type']
                if combat_type == 'aggressive':
                    strategy = AggressiveStrategy()
                elif combat_type == 'defensive':
                    strategy = DefensiveStrategy()
                elif combat_type == 'balanced':
                    strategy = BalancedStrategy()
                else:
                    print(f"Unknown combat type: {combat_type}")
                    return {}

                command = FightCommand(
                    enemy_name=command_data['enemy'],
                    enemy_hp=command_data.get('enemy_hp', 50),
                    enemy_attack=command_data.get('enemy_attack', 10),
                    combat_strategy=strategy
                )
            else:
                print(f"Unknown command type: {command_data['type']}")
                return {}

            if command:
                command.execute(self.player)

        return choice['result']

