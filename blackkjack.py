import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank['rank']} of {self.suit}"

class Deck:
    def __init__(self):
        suits = ['spades', 'hearts', 'clubs', 'diamonds']
        ranks = [
            {'rank': 'A', 'value': 11},
            {'rank': 2, 'value': 2},
            {'rank': 3, 'value': 3},
            {'rank': 4, 'value': 4},
            {'rank': 5, 'value': 5},
            {'rank': 6, 'value': 6},
            {'rank': 7, 'value': 7},
            {'rank': 8, 'value': 8},
            {'rank': 9, 'value': 9},
            {'rank': 10, 'value': 10},
            {'rank': 'J', 'value': 10},
            {'rank': 'Q', 'value': 10},
            {'rank': 'K', 'value': 10},
        ]
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        if len(self.cards) >= 1:
            random.shuffle(self.cards)

    def deal(self, number):
        cards_dealt = []
        for _ in range(number):
            if len(self.cards) > 0:
                cards_dealt.append(self.cards.pop())
        return cards_dealt

class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer

    def add_card(self, card_list):
        self.cards.extend(card_list)

    def calculate_value(self):
        self.value = 0
        has_ace = False
        for card in self.cards:
            self.value += card.rank['value']
            if card.rank['rank'] == 'A':
                has_ace = True
        if has_ace and self.value > 21:
            self.value -= 10

    def get_value(self):
        self.calculate_value()
        return self.value

    def is_blackjack(self):
        return self.get_value() == 21

    def display(self, show_all_dealer_cards=False):
        print(f"{'Dealer' if self.dealer else 'Your'} hand:")
        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer and not show_all_dealer_cards:
                print("Hidden")
            else:
                print(card)
        if not self.dealer:
            print("Value:", self.get_value())
        print()

class Game:
    def play(self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
            except ValueError:
                print("You must enter a number")

        while game_number < games_to_play:
            game_number += 1
            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for _ in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print("\n" + "*" * 30)
            print(f"Game {game_number} of {games_to_play}")

            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Please choose 'Hit' or 'Stand': ").lower()
                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            while dealer_hand.get_value() < 17:
                dealer_hand.add_card(deck.deal(1))

            dealer_hand.display(show_all_dealer_cards=True)

            if not self.check_winner(player_hand, dealer_hand, game_over=True):
                self.check_winner(player_hand, dealer_hand, game_over=True)

    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("Dealer wins!")
                return True
            elif dealer_hand.get_value() > 21:
                print("Player wins!")
                return True
            elif player_hand.is_blackjack() and dealer_hand.is_blackjack():
                print("Both players have Blackjack! It's a tie!")
                return True
            elif player_hand.is_blackjack():
                print("You have Blackjack! You win!")
                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has Blackjack! Dealer wins!")
                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("Player wins!")
            elif player_hand.get_value() == dealer_hand.get_value():
                print("It's a tie!")
            else:
                print("Dealer wins!")
            return True
        return False

# Run the game
game = Game()
game.play()






'''
deck1 = deck()
deck2 = deck()

deck2.shuffle()

#print(deck1.cards)
print(deck2.cards)







    cards_dealt = deal(2)
    print (cards_dealt)

    card = cards_dealt[0]

    rank = card[1]

    if rank == 'A':
        value = 11
    elif rank == 'J' or rank == 'Q' or rank == 'K':
        value = 10
    else:
        value = rank

    rank_dict = {'rank': rank, 'value' : value}
    print (rank_dict['rank'])
    print (rank_dict['value'])
    #print(card)

 '''