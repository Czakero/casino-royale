import termcolor


def get_lines(cards):

    table = [57 * 'P']
    CARD_HEIGHT = 8

    card1_index = 0
    card2_index = 1
    card3_index = 2
    card4_index = 3
    card5_index = 4
    number_index = 0

    card1 = open('cards/' + str(cards[card1_index][number_index]) + '.txt')
    card2 = open('cards/' + str(cards[card2_index][number_index]) + '.txt')
    card3 = open('cards/' + str(cards[card3_index][number_index]) + '.txt')
    card4 = open('cards/' + str(cards[card4_index][number_index]) + '.txt')
    card5 = open('cards/' + str(cards[card5_index][number_index]) + '.txt')

    for i in range(CARD_HEIGHT):

        table.append('PP' + card1.readline().strip()
                   + 'PP' + card2.readline().strip()
                   + 'PP' + card3.readline().strip()
                   + 'PP' + card4.readline().strip()
                   + 'PP' + card5.readline().strip()
                   + 'PP')
    
    table.append(57 * 'P')

    card1.close()
    card2.close()
    card3.close()
    card4.close()
    card5.close()

    return table

    #get_lines([[2, "heart"], [2, "club"], [2, "diamond"], [2, "spade"], [2, "heart"]])
def print_hand(hand, hidden=False):

    BACKGROUND = 'on_green'
    CARD_BACKGROUND = 'on_white'

    table = get_lines(hand)

    for lane in table:
        i = 0
        for symbol in lane:

            if not hidden:

                letter_index = i
                i += 1

                if symbol == 'D':
                    symbol, color = get_symbol(hand, letter_index)
                
                temp, color = get_symbol(hand, letter_index)

                if symbol in ['P', 'X']:
                    print(termcolor.colored(' ', on_color=BACKGROUND), end='')
                elif symbol == 'W':
                    print(termcolor.colored(' ', on_color=CARD_BACKGROUND), end='')
                else:
                    print(termcolor.colored(symbol, color=color, on_color=CARD_BACKGROUND), end='')

            else:

                if symbol == 'P':
                    print(termcolor.colored(' ', on_color=BACKGROUND), end='')

                else:
                    print(termcolor.colored('X', 'magenta', 'on_grey'), end='')

        print('')


def get_symbol(cards, letter_index):

    positions = get_card_positions()

    card1_positions = positions[0]
    card2_positions = positions[1]
    card3_positions = positions[2]
    card4_positions = positions[3]
    card5_positions = positions[4]

    if letter_index in card1_positions:
        sym, color = get_picture(letter_index, card1_positions, cards, 0)

    elif letter_index in card2_positions:
        sym, color = get_picture(letter_index, card2_positions, cards, 1)

    elif letter_index in card3_positions:
        sym, color = get_picture(letter_index, card3_positions, cards, 2)

    elif letter_index in card4_positions:
        sym, color = get_picture(letter_index, card4_positions, cards, 3)

    elif letter_index in card5_positions:
        sym, color = get_picture(letter_index, card5_positions, cards, 4)
    else:
        sym, color = ' ', ' '

    return sym, color


def get_picture(index, card_positions, cards, num):

    diamond = chr(9830)
    club = chr(9827)
    heart = chr(9829)
    spade = chr(9824)

    if index in card_positions:
        if cards[num][1] == 'diamond':
            return diamond, 'red'
        elif cards[num][1] == 'club':
            return club, 'grey'
        elif cards[num][1] == 'heart':
            return heart, 'red'
        elif cards[num][1] == 'spade':
            return spade, 'grey'


def get_card_positions():
    
    positions = []
    one_card = []

    cards_amount = 5
    card_width = 9

    init = 1

    for i in range(cards_amount):
        for j in range(card_width):
            init += 1
            one_card.append(init)
        positions.append(one_card)
        one_card = []
        init += 2
    
    return positions