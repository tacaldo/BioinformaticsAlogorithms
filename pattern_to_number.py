def pattern_to_number(pattern):
    if pattern == '':
        return 0

    length_of_pattern = len(pattern)
    symbol = pattern[length_of_pattern - 1]
    prefix = pattern[0:length_of_pattern - 1]

    return 4 * pattern_to_number(prefix) + symbol_to_number(symbol)


def symbol_to_number(symbol):  # A -> 0, C -> 1, G -> 2, T -> 3
    if symbol == 'A':
        return 0
    elif symbol == 'C':
        return 1
    elif symbol == 'G':
        return 2
    elif symbol == 'T':
        return 3

    return -1



# textIn = input('Enter text to scan for pattern_to_number:')
#
# result = pattern_to_number(textIn)
#
# print('result for ' + textIn + ' is: ' + str(result))


