import random
import time
import os
import json
from platform import system
from datetime import datetime

gaslight_prompts = [
    # Funny/Weird
    "I’ve never seen a clock in real life.",
    "I can communicate with squirrels.",
    "I don’t understand how stairs work.",
    "I’ve never laughed—ever.",
    "I sleep standing up like a horse.",
    "I’m convinced clouds are just government drones.",
    "I’ve never used a door handle.",
    "I think the alphabet has 30 letters.",
    "I can only count in Roman numerals.",
    "I’ve never seen my own reflection.",
    
    # Dramatic/Over-the-Top
    "I’m actually a retired spy.",
    "I was raised by wolves until age 12.",
    "I’m allergic to lies (but only on Tuesdays).",
    "I’ve never felt the emotion of ‘joy.’",
    "I’m legally required to wear sunglasses indoors.",
    "I can only speak in rhymes after midnight.",
    "I’m in witness protection—but I can’t say why.",
    "I’ve never met my identical twin.",
    "I get all my news from fortune cookies.",
    "I’ve never blinked—I just close my eyes manually.",
    
    # Mind-Bending
    "I remember the future.",
    "I’ve never experienced time linearly.",
    "I’m convinced yesterday didn’t happen.",
    "I can hear colors.",
    "I don’t believe in the concept of ‘names.’",
    "I think mirrors are portals to another dimension.",
    "I’ve never had a thought of my own.",
    "I’m pretty sure I’m a ghost.",
    "I can taste words.",
    "I’ve never been ‘awake’—this is all a dream.",
    
    # Drinking-Specific
    "I’ve never had a hangover.",
    "I can drink an entire bottle of hot sauce.",
    "I’ve never spilled a drink in my life.",
    "I only drink liquids through a straw.",
    "I’m convinced water is alcoholic.",
    
    # Bonus (New Additions)
    "I’m fluent in 15 languages, all of them fictional.",
    "I can only walk backward on weekends.",
    "I’ve never worn matching socks.",
    "I believe the moon is a hologram.",
    "I can only eat food that’s blue.",
    "I’ve never used a smartphone.",
    "I’m convinced all birds are robots.",
    "I can only whisper in the presence of cats.",
    "I’ve never had a birthday.",
    "I think gravity is just a suggestion."
]

class GaslightGame:
    SAVE_FILE = "gaslight_save.json"
    
    def __init__(self):
        self.players = []
        self.scores = {}
        self.current_round = 1
        self.max_rounds = 3
        self.current_player_index = 0
        self.penalty_mode = "seconds"
        self.custom_penalties = [
            "Take {difference} second drink",
            "Do {difference} push-ups",
            "Sing for {difference} seconds",
            "Truth or Dare penalty"
        ]
        
    def clear_screen(self):
        os.system('cls' if system() == "Windows" else 'clear')
    
    def setup_penalties(self):
        self.clear_screen()
        print("⚖️ DRINKING PENALTY MODES:")
        print("1. Timed drinks (default)")
        print("2. Push-up punishment")
        print("3. Singing penalty")
        print("4. Truth or Dare")
        print("5. Custom message")
        
        choice = input("\nSelect penalty mode (1-5): ").strip()
        if choice == "1":
            self.penalty_mode = "seconds"
        elif choice == "2":
            self.penalty_mode = "pushups"
        elif choice == "3":
            self.penalty_mode = "singing"
        elif choice == "4":
            self.penalty_mode = "truth_dare"
        else:
            self.penalty_mode = "custom"
            print("\n💬 Enter custom penalty text (use {difference} for score difference)")
            print("Example: 'Do {difference} jumping jacks'")
            self.custom_penalties.append(input("> "))
    
    def setup_players(self):  # THIS WAS MISSING IN YOUR VERSION
        self.clear_screen()
        print("🎳 GASLIGHTING DRINKING GAME SETUP 🍻")
        
        if os.path.exists(self.SAVE_FILE):
            load = input("Load previous game? (y/n): ").lower() == 'y'
            if load and self.load_game():
                return
        
        num_players = int(input("\nHow many players? "))
        print("\nEnter player names (like bowling teams!):")
        self.players = [input(f"Player {i+1} name: ") for i in range(num_players)]
        self.scores = {player: 0 for player in self.players}
        random.shuffle(self.players)
        print(f"\n🎳 Turn order: {' → '.join(self.players)}")
        input("\nPress Enter to start...")
    
    def load_game(self):
        try:
            with open(self.SAVE_FILE, 'r') as f:
                save_data = json.load(f)
            
            self.players = save_data["players"]
            self.scores = save_data["scores"]
            self.current_round = save_data["current_round"]
            self.current_player_index = save_data["current_player_index"]
            
            print(f"🔄 Loaded game from {save_data['timestamp']}")
            print(f"Players: {', '.join(self.players)}")
            print(f"Current round: {self.current_round}")
            time.sleep(3)
            return True
        except:
            print("❌ No saved game found")
            time.sleep(2)
            return False
    
    def save_game(self):
        save_data = {
            "players": self.players,
            "scores": self.scores,
            "current_round": self.current_round,
            "current_player_index": self.current_player_index,
            "timestamp": str(datetime.now())
        }
        with open(self.SAVE_FILE, 'w') as f:
            json.dump(save_data, f)
    
    def play_turn(self, player):
        self.clear_screen()
        print(f"\n🎭 {player}'s turn! (Round {self.current_round}/{self.max_rounds})")
        input("Press Enter to draw your prompt...")
        
        prompt = random.choice(gaslight_prompts)
        print(f"\n🚨 YOUR MISSION:\n»» {prompt} ««")
        
        print("\n⏳ 30 seconds to gaslight!")
        for sec in range(30, 0, -1):
            print(f"{sec:2d}", end=' ', flush=True)
            time.sleep(1)
        
        believers = int(input("\n\nHow many players believed you? "))
        points = believers * 10
        self.scores[player] += points
        print(f"➕ {player} earned {points} points! (Total: {self.scores[player]})")
        self.save_game()
        time.sleep(2)
    
    def play_round(self):
        for i, player in enumerate(self.players):
            self.current_player_index = i
            self.play_turn(player)
        self.current_round += 1
    
    def show_scores(self):
        self.clear_screen()
        print("\n📊 CURRENT STANDINGS:")
        sorted_players = sorted(self.scores.items(), key=lambda x: -x[1])
        for rank, (player, score) in enumerate(sorted_players, 1):
            print(f"{rank}. {player}: {score} pts")
        
        loser = min(self.scores, key=self.scores.get)
        penalty = max(1, max(self.scores.values()) - self.scores[loser])
        print(f"\n🍺 Current penalty: {self.get_penalty_text(penalty)}")
        input("\nPress Enter to continue...")
    
    def get_penalty_text(self, difference):
        if self.penalty_mode == "seconds":
            return f"Drink for {difference} seconds"
        elif self.penalty_mode == "pushups":
            return f"Do {difference} push-ups"
        elif self.penalty_mode == "singing":
            return f"Sing for {difference} seconds"
        elif self.penalty_mode == "truth_dare":
            return f"Truth or Dare (x{difference})"
        else:
            return self.custom_penalties[-1].format(difference=difference)
    
    def declare_winner(self):
        self.clear_screen()
        winner = max(self.scores, key=self.scores.get)
        loser = min(self.scores, key=self.scores.get)
        difference = max(1, self.scores[winner] - self.scores[loser])
        
        print("="*50)
        print(f"🏆 FINAL RESULTS 🏆".center(50))
        print("="*50)
        for player, score in sorted(self.scores.items(), key=lambda x: -x[1]):
            print(f"{player.upper():<25}: {score} pts".center(50))
        print("="*50)
        print(f"\n🔥 {winner.upper()} WINS!".center(50))
        print(f"💀 {loser.upper()} GETS: {self.get_penalty_text(difference)}!".center(50))
        print("="*50 + "\n")
        
        if os.path.exists(self.SAVE_FILE):
            os.remove(self.SAVE_FILE)
    
    def play(self):
        self.setup_penalties()
        self.setup_players()  # Fixed this line
        
        while self.current_round <= self.max_rounds:
            self.play_round()
            if self.current_round <= self.max_rounds:
                self.show_scores()
        
        self.declare_winner()

if __name__ == "__main__":
    game = GaslightGame()
    game.play()