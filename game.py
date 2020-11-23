from player import Player
import random
import math


class Game():
    def __init__(self,player_count=2):
        self.players = [Player() for i in range(player_count)]
        for i in range(20):
            self.shuffle()
            deck = self.cards[:random.randint(2,6)]
            print('Deck: ',self.readableCardFormat(deck))
            print('Winner: ',self.readableCardFormat(self.winning_Card(deck)))

    def shuffle(self):
        self.cards = list(range(66))
        #print(self.cards)
        random.shuffle(self.cards)
        #print(self.readableCardFormat(self.cards))
        #print(self.cards)

    def winning_Card(self,card_list):
        winning_card = card_list[0]
        color = -1
        if 64 in card_list:
            for card in card_list:
                if card == 4*13+5 or card == 4*13+6:
                    return card
        for card in card_list:
            if color == -1 and math.floor(card / 13)<4:
                color = math.floor(card / 13)
            winning_card = self.compare_Card(winning_card,card,color)
        return winning_card

    def compare_Card(self,card0,card1,color):
        return card1 if self.card_to_value(card1,color)>self.card_to_value(card0,color) else card0

    def card_to_value(self,card,color):
        type = math.floor(card / 13)
        value = card % 13
        if type < 3:
            if color != -1:
                return value * (type==color)
            return value
        if type == 3:
            return 13 + value
        if type == 4:
            return [0,0,0,0,0,26,26,27,27,27,27,27,28][value]
        if type ==5:
            return [0,0,27][value]


    def readableCardFormat(self,card):
        if isinstance(card,list):
            return [self.readableCardFormat(c) for c in card]
        type = math.floor(card/13)
        value = card%13
        if type < 4:
            return ['blue {}','red {}','yellow {}','black {}'][type].format(value+1)
        if type == 4:
            return ['flag','flag','flag','flag','flag','mermaid','mermaid','pirate','pirate','pirate','pirate','pirate','scull king'][value]
        if type == 5:
            return ['scary mary - undecided','scary mary - flag','scary mary - pirate'][value]



Game()