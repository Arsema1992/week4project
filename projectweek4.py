import random

class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Clubs", "Diamonds", "Hearts", "Spades"]:
            for rank in range(1, 14):
                self.cards.append((suit, rank))
        self.shuffle()

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

    def cards_left(self):
        return len(self.cards)
class Player1:
    def __init__(self):
        self.hand = []

    def add_card(self, card):
        self.hand.append(card)

    def get_hand_value(self):
        hand_value = 0
        num_aces = 0
        for card in self.hand:
            if card[1] == 1:
                num_aces += 1
                hand_value += 11
            elif card[1] > 10:
                hand_value += 10
            else:
                hand_value += card[1]
        while hand_value > 21 and num_aces > 0:
            hand_value -= 10
            num_aces -= 1
        return hand_value

class Dealer1:
    def __init__(self, deck):
        self.deck = deck
        self.player_hand = []
        self.dealer_hand = []
        self.deal_cards()

    def deal_cards(self):
        self.player_hand = [self.deck.draw_card(), self.deck.draw_card()]
        self.dealer_hand = [self.deck.draw_card(), self.deck.draw_card()]

    def get_player_hand_value(self):
        return sum(card[1] for card in self.player_hand)

    def get_dealer_hand_value(self):
        return sum(card[1] for card in self.dealer_hand)

    def player_hit(self):
        self.player_hand.append(self.deck.draw_card())

    def dealer_hit(self):
        self.dealer_hand.append(self.deck.draw_card())
def play_game():
    deck = Deck()
    dealer = Dealer1(deck)
    player = Player1()

    print("Dealer's hand: [{}][?]".format(dealer.dealer_hand[0]))
    print("Your hand: [{}][{}]".format(player.hand[0], player.hand[1]))

    if player.get_hand_value() == 21:
        print("Blackjack! You win!")
        return

    while True:
        action = input("Do you want to hit or stand? ")
        if action == "hit":
            player.add_card(deck.draw_card())
            print("Your hand")