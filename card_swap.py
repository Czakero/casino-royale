import pool_cards
from operator import itemgetter
import curses


def card_swap(hand, cards_pool):

    list_of_cards_to_change = ask_for_cards()

    if_card_swap = True
    while if_card_swap:
        if_card_swap = False

        if len(list_of_cards_to_change) == 0:

            break

        if len(list_of_cards_to_change) >= len(hand):
            print("You don't have so many cards!")
            list_of_cards_to_change = ask_for_cards()
            if_card_swap = True

        elif list_of_cards_to_change[-1] > len(hand) - 1:
            print("You don't have so many cards!")
            list_of_cards_to_change = ask_for_cards()
            if_card_swap = True

        else:
            for index in list_of_cards_to_change:
                hand.remove(hand[index])

    hand += pool_cards.get_hand(cards_pool, n=len(list_of_cards_to_change) + 1)
    hand = sorted(hand, key=itemgetter(0))

    return hand, cards_pool


def ask_for_cards():

    list_of_cards_to_change = []
    cards_to_change = input("Which cards you want to change? If none just press enter: ")

    if cards_to_change == "":

        return list_of_cards_to_change

    if_ask_for_cards = True 
    while if_ask_for_cards:
        if_ask_for_cards = False

        for card in cards_to_change.split(" "):
            try:
                int(card)

            except ValueError:
                cards_to_change = input("Which cards you want to change? ")
                if_ask_for_cards = True

    for card in cards_to_change.split(" "):
        list_of_cards_to_change.append(int(card) - 1)

    list_of_cards_to_change = set(list_of_cards_to_change)
    list_of_cards_to_change = list(list_of_cards_to_change)
    list_of_cards_to_change = sorted(list_of_cards_to_change, reverse=True)

    return list_of_cards_to_change
