def check_if_poker(hand):

    poker_combo = 0
    suits_combo = 0
    cards_values = []
    straight = False
    flush = False
    VALUE_INDEX = 0
    SUIT_INDEX = 1
    result = "null"

    for card in hand:
        cards_values.append(card[0])

    for i in range(len(cards_values) - 1):
        if cards_values[i] == cards_values[i + 1] - 1:
            poker_combo += 1
        elif cards_values[i] == 5 and cards_values[i + 1] == 14:
            poker_combo += 1

    if poker_combo == 4:
        straight = True
        result = "straight"

    suit = hand[0][SUIT_INDEX]

    for card in hand:
        if suit == card[SUIT_INDEX]:
            suits_combo += 1
            if suits_combo == 5:
                flush = True
                result = "flush"

    if straight and flush:
        result = "royal flush"

    return result
