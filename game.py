import random

# Rules
HAND_SIZE = 3
POINTS_TO_WIN = 3

# Cards
green_cards = ["Happy",
               "Smelly",
               "Angry",
               "Gigantic",
               "Painful",
               "Cheap",
               "Mighty",
               "Weak",
               "Weird"]

red_cards = ["Birthday party",
             "Windows XP",
             "Toyota Prius",
             "Soiled diaper",
             "School cafeteria food",
             "Rotting fish",
             "Facebook",
             "Bears",
             "Your mom",
             "The Death Star"]


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
        self.points = 0
        
    def play_card(self):
        for i, c in enumerate(self.cards):
            print(i, c)

        n = input("Which card? ")
        n = int(n)

        return self.cards[n]
    
class Game:
    def __init__(self):
        self.players = []
        self.green_cards = green_cards
        self.red_cards = red_cards
    
    def start(self):
        num_players = input("How many players? ")
        num_players = int(num_players)
        
        for i in range(num_players):
            name = input("Enter the name for player {}:".format(i))
            self.players.append(Player(name))
        
        self.restart()

    def restart(self):
        for p in self.players:
            p.cards = []
            p.points = 0

        random.shuffle(self.green_cards)
        random.shuffle(self.red_cards)

        self.green_index = 0
        self.deal()
        
    def deal(self):
        for _ in range(HAND_SIZE):
            for p in self.players:
                p.cards.append(random.choice(red_cards))
                
    def get_next_green_card(self):
        card = self.green_cards[self.green_index]
        self.green_index = (self.green_index + 1) % len(self.green_cards)
            
        return card    
    
    def get_winner(self):
        for p in self.players:
            if p.points == POINTS_TO_WIN:
                return p
            
        return None
    
    def pick_best(self, plays):
        random.shuffle(plays)

        for i, p in enumerate(plays):
            print(i, p['card'])

        best = input("Which is best? ")
        best = int(best)

        return plays[best]['player']
    
    def play(self):
        winner = None
        
        while winner == None:
            green = self.get_next_green_card()
            print("Green: {}".format(green))

            plays = []
            for p in self.players:
                print(p.name)
                c = p.play_card()
                plays.append({"player": p, "card": c})

            best_player = self.pick_best(plays)
            best_player.points += 1
            
            winner = self.get_winner()


        print("{} is the winner".format(winner.name))
        
if __name__ == "__main__":
    g = Game()
    g.start()
    g.play()
