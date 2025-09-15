import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal_card(self):
        return self.cards.pop()

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def get_value(self):
        value = 0
        aces = 0
        
        for card in self.cards:
            if card.rank == 'A':
                aces += 1
                value += 11
            else:
                value += card.value()
        
        while value > 21 and aces > 0:
            value -= 10
            aces -= 1
        
        return value
    
    def is_blackjack(self):
        return len(self.cards) == 2 and self.get_value() == 21
    
    def is_bust(self):
        return self.get_value() > 21
    
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)

class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
    
    def deal_initial_cards(self):
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
    
    def show_hands(self, hide_dealer_card=True):
        print(f"\nPlayer's hand: {self.player_hand} (Value: {self.player_hand.get_value()})")
        
        if hide_dealer_card:
            print(f"Dealer's hand: {self.dealer_hand.cards[0]}, [Hidden Card]")
        else:
            print(f"Dealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.get_value()})")
    
    def player_turn(self):
        while True:
            if self.player_hand.is_bust():
                print("Player busts!")
                return False
            
            action = input("\nDo you want to (h)it or (s)tand? ").lower()
            
            if action == 'h':
                self.player_hand.add_card(self.deck.deal_card())
                self.show_hands()
            elif action == 's':
                break
            else:
                print("Invalid input. Please enter 'h' for hit or 's' for stand.")
        
        return not self.player_hand.is_bust()
    
    def dealer_turn(self):
        print("\nDealer's turn:")
        self.show_hands(hide_dealer_card=False)
        
        while self.dealer_hand.get_value() < 17:
            print("Dealer hits...")
            self.dealer_hand.add_card(self.deck.deal_card())
            print(f"Dealer's hand: {self.dealer_hand} (Value: {self.dealer_hand.get_value()})")
        
        if self.dealer_hand.get_value() >= 17:
            print("Dealer stands.")
    
    def determine_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        
        print(f"\nFinal Results:")
        print(f"Player: {player_value}")
        print(f"Dealer: {dealer_value}")
        
        if self.player_hand.is_blackjack() and self.dealer_hand.is_blackjack():
            return "Push! Both have blackjack."
        elif self.player_hand.is_blackjack():
            return "Blackjack! Player wins!"
        elif self.dealer_hand.is_blackjack():
            return "Dealer has blackjack. Dealer wins!"
        
        if self.player_hand.is_bust():
            return "Player busts. Dealer wins!"
        elif self.dealer_hand.is_bust():
            return "Dealer busts. Player wins!"
        
        if player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "Push! It's a tie."
    
    def play_round(self):
        print("=== New Blackjack Round ===")
        
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.deal_initial_cards()
        
        self.show_hands()
        
        if self.player_hand.is_blackjack() or self.dealer_hand.is_blackjack():
            self.show_hands(hide_dealer_card=False)
            print(self.determine_winner())
            return
        
        if self.player_turn():
            self.dealer_turn()
        
        print(self.determine_winner())
    
    def play(self):
        print("Welcome to Blackjack!")
        print("Goal: Get as close to 21 as possible without going over.")
        print("Face cards are worth 10, Aces are worth 1 or 11.")
        
        while True:
            if len(self.deck.cards) < 10:
                print("\nReshuffling deck...")
                self.deck = Deck()
            
            self.play_round()
            
            play_again = input("\nDo you want to play another round? (y/n): ").lower()
            if play_again != 'y':
                break
        
        print("Thanks for playing!")

if __name__ == "__main__":
    game = BlackjackGame()
    game.play()