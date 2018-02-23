def check_the_same_cards(hand):

    list_of_cards = []
    cards_values = []
    y = ''
    x = ''
    result = 'null'
    VALUE_INDEX = 0

    for card in hand:
        cards_values.append(card[VALUE_INDEX])

    for element in cards_values:
        if cards_values.count(element) == 2:
            y = "pair"
            result = y
            list_of_cards.append(element)
            cards_values.remove(element)
            if len(cards_values) == 3:
                result = "two pairs"

        elif cards_values.count(element) == 3:
            triple_value = element
            x = "triple"
            result = x
            list_of_cards.append(element)

        elif cards_values.count(element) == 4:
            result = "four of kind"
            list_of_cards.append(element)

        if y == "pair" and x == "triple":
            list_of_cards = []
            list_of_cards.append(triple_value)
            result = "full"

    return result, list_of_cards
