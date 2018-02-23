import pool_cards
from combos import get_value, get_combo, compare, compare_hands
import print_table
from question import question_about_playing
from card_swap import card_swap
import os
import time


def ui(hand_p1, hidden_cards_p1, hand_p2, hidden_cards_p2):

    os.system("clear")
    print_table.print_hand(hand_p1, hidden_cards_p1)
    print_table.print_hand(hand_p2, hidden_cards_p2)


def time_sleep():

    for i in range(5, 0, -1):
        print("Player cards reveal in {0} seconds".format(i))
        time.sleep(1)


def return_cards():

    cards = pool_cards.get_cards()
    hand_p1 = pool_cards.get_hand(cards)
    hand_p2 = pool_cards.get_hand(cards)

    return hand_p1, hand_p2, cards


def configuration_print_list(hand_p1, hand_p2):

    both_hidden = [hand_p1, True, hand_p2, True]
    both_show = [hand_p1, False, hand_p2, False]
    p1_hidden_cards = [hand_p1, True, hand_p2, False]
    p2_hidden_cards = [hand_p1, False, hand_p2, True]

    configuration_list = [both_hidden, both_show, p1_hidden_cards, p2_hidden_cards]

    return configuration_list


def print_game(configuration_list, hand_p1, hand_p2, cards):

    BOTH_HIDDEN_INDEX = 0
    BOTH_SHOW_INDEX = 1
    P1_HIDDEN_CARDS_INDEX = 2
    P2_HIDDEN_CARDS_INDEX = 3

    ui(*configuration_list[BOTH_HIDDEN_INDEX])
    time_sleep()
    ui(*configuration_list[P2_HIDDEN_CARDS_INDEX])
    hand_p1, cards = card_swap(hand_p1, cards)
    ui(*configuration_list[BOTH_HIDDEN_INDEX])
    time_sleep()
    ui(*configuration_list[P1_HIDDEN_CARDS_INDEX])
    hand_p2, cards = card_swap(hand_p2, cards)
    ui(*configuration_list[BOTH_SHOW_INDEX])

    return hand_p1, hand_p2, cards


def main():

    gameplay = True
    while gameplay:

        hand_p1, hand_p2, cards = return_cards()
        configuration_list = configuration_print_list(hand_p1, hand_p2)
        hand_p1, hand_p2, cards = print_game(configuration_list, hand_p1, hand_p2, cards)

        result_p1, list_of_cards_p1 = get_value(*get_combo(hand_p1))
        result_p2, list_of_cards_p2 = get_value(*get_combo(hand_p2))

        if result_p1 == result_p2:
            straight = 4
            flush = 5
            royal_flush = 8
            if result_p1 not in [straight, flush, royal_flush]:
                result_p1, result_p2 = compare(list_of_cards_p1, list_of_cards_p2, hand_p1, hand_p2)

            else:
                CARD_VALUE = 0
                LAST_CARD_INDEX = -1
                result_p1, result_p2 = compare_hands(hand_p1[LAST_CARD_INDEX][CARD_VALUE],
                                                     hand_p2[LAST_CARD_INDEX][CARD_VALUE])

        if result_p1 > result_p2:
            print('Player 1 win!')
            gameplay = question_about_playing()

        elif result_p1 == result_p2:
            print("Draw!")
            gameplay = question_about_playing()

        else:
            print('Player 2 win!')
            gameplay = question_about_playing()


if __name__ == '__main__':
    main()
