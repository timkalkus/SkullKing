import random
import math
class Player():
    def __init__(self):
        do = 0
        # print('TODO')
    def set_hand(self,cards):
        self.cards = cards
        self.cards_temp = cards
        self.wins = 0
    def get_prediction(self):
        return random.randint(0,len(self.cards))
    def add_win(self):
        self.wins = self.wins + 1
    def get_win(self):
        return self.wins
    def turn(self,color=-1):
        allowed_cards=[]
        if color !=-1:
            allowed_cards.append([card for card in self.cards if math.floor(card / 13)==color])
        if len(allowed_cards):
            allowed_cards.append([card for card in self.cards if math.floor(card / 13)>3])
        else:
            allowed_cards = self.cards
        random.shuffle(allowed_cards)
        self.cards = [card for card in self.cards if card != allowed_cards[0]]

        return allowed_cards[0]
