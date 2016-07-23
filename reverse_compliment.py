textIn = input('Enter DNA text to reverse:')


def reverse_compliment(text):
    """doc code here.."""
    buffer = []
    for i in range(0, len(text)):  # A - T, G - C, complements
        if text[i] == 'A':
            buffer.append('T')
        elif text[i] == 'T':
            buffer.append('A')
        elif text[i] == 'G':
            buffer.append('C')
        elif text[i] == 'C':
            buffer.append('G')
    return buffer


result = reverse_compliment(textIn)
final_result = ''

print('reverse compliment of: ' + textIn + '\nis: ' + str(reverse_compliment(textIn)))

for i in reversed(result):
    final_result += i

print('\n\nfinal result is: ' + final_result)
