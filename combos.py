from poker_combinations import check_if_poker
from pairs import check_the_same_cards


def get_value(result, list_of_cards):

    results = ('null', 'pair', 'two pairs', 'triple', 'straight',
               'flush', 'full', 'four of kind', 'royal flush')

    value = results.index(result)

    return value, list_of_cards


def get_combo(hand):

    if check_if_poker(hand) == 'null':
        result, list_of_cards = check_the_same_cards(hand)
    else:
        result = check_if_poker(hand)
        list_of_cards = []

    return result, list_of_cards


def compare(list_of_cards_p1, list_of_cards_p2, hand_p1, hand_p2):

    both_cards_values = create_list(hand_p1, hand_p2)

    if len(list_of_cards_p1) == 0:
        result_p1, result_p2 = compare_hands(hand_p1[-1][0], hand_p2[-1][0])

        return result_p1, result_p2

    elif len(list_of_cards_p1) == 1:
        result_p1, result_p2 = check_if_pair_is_equal(list_of_cards_p1, list_of_cards_p2, both_cards_values, n=-1)

        return result_p1, result_p2

    elif len(list_of_cards_p1) == 2:
        if list_of_cards_p1[-1] > list_of_cards_p2[-1]:

            return 1, 0

        elif list_of_cards_p1[-1] == list_of_cards_p2[-1]:
            result_p1, result_p2 = check_if_pair_is_equal(list_of_cards_p1, list_of_cards_p2, both_cards_values)

            return result_p1, result_p2

        else:

            return 0, 1
    else:
        if list_of_cards_p1[-1] > list_of_cards_p2[-1]:

            return 1, 0

        else:

            return 0, 1


def check_if_pair_is_equal(list_of_cards_p1, list_of_cards_p2, both_cards_values, n=0):

    if list_of_cards_p1[n] > list_of_cards_p2[n]:

        return 1, 0

    elif list_of_cards_p1[n] == list_of_cards_p2[n]:
        both_cards_values[0] = remove_from_list(both_cards_values[0], list_of_cards_p1)
        both_cards_values[1] = remove_from_list(both_cards_values[1], list_of_cards_p2)
        result_p1, result_p2 = compare_hands(both_cards_values[0][-1], both_cards_values[1][-1])

        return result_p1, result_p2

    else:

        return 0, 1


def create_list(hand_p1, hand_p2):

    cards_values_p1 = []
    cards_values_p2 = []

    for i in range(len(hand_p1)):
        cards_values_p1.append(hand_p1[i][0])
        cards_values_p2.append(hand_p2[i][0])

    both_cards_values = [cards_values_p1, cards_values_p2]

    return both_cards_values


def compare_hands(hand_p1, hand_p2):

    if hand_p1 > hand_p2:

        return 1, 0

    elif hand_p1 == hand_p2:

        return 0, 0

    else:

        return 0, 1

def remove_from_list(cards_values, list_of_cards):

    for element in cards_values:
        if element in list_of_cards:
            cards_values.remove(element)

    return cards_values
