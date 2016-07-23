import pattern_to_number


def computing_frequencies(text, k):  #
    frequency_array = []
    pattern = ''
    for i in range(0, 4 ** k):
        frequency_array.append(0)
    for i in range(0, len(text) - k):
        pattern = text[i:k + 1]
        j = pattern_to_number.pattern_to_number(pattern)
        frequency_array[j] = int(frequency_array[j]) + 1

    return frequency_array
