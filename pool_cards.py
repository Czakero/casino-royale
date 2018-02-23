import random
from operator import itemgetter


def get_cards():

    CARDS = []
    SUITS = ('diamond', 'club', 'heart', 'spade')

    for number in range(2, 15, 1):
        for suit in SUITS:
            CARDS.append([number, suit])
    
    return CARDS


def get_hand(cards_pool, n=6):
    
    hand = []
    for i in range(1, n, 1):
        
        card_index = random.randint(0, len(cards_pool)) - 1
        card = cards_pool[card_index]

        hand.append(card)
        cards_pool.remove(card)
    
    hand = sorted(hand, key=itemgetter(0))

    return hand