def number_to_pattern(index, k):
    if k == 1:
        return number_to_symbol(index)
    x = divmod(index, 4)
    prefix_index = x[0]  # Quotient
    r = x[1]  # Remainder
    symbol = number_to_symbol(r)
    prefix_pattern = number_to_pattern(prefix_index, k - 1)

    return prefix_pattern + symbol


def number_to_symbol(number):  # A <- 0, C <- 1, G <- 2, T <- 3
    if number == 0:
        return 'A'
    elif number == 1:
        return 'C'
    elif number == 2:
        return 'G'
    elif number == 3:
        return 'T'
    return 0

# print(number_to_pattern(7023, 11))