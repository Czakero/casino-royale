import termcolor

first_tabs = 24
second_tabs = 24
background = 'on_green'

MENU = ['Poker', 'Quit ']
values = []

for item in MENU:
    values.append(0)

values[0] = 1

for title in MENU:
    print(termcolor.colored(' ' * first_tabs, on_color=background), end='')
    print(termcolor.colored(title, 'blue', background), end='')
    print(termcolor.colored(' ' * second_tabs, on_color=background), end='')
    print()