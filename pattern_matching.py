
def patternCount(text, pattern):
    count = 0
    patternlen = len(pattern)
    textlen = len(text)
    pattern_locations = []

    for i in range(0, textlen):
        patternInText = text[i:i + patternlen]  # slide window for text
        if text[i:i + patternlen] == pattern:
            count += 1
            pattern_locations.append(i)

    return pattern_locations


# textIn = input('Enter text to scan: ')

f = open('C:\BioInformatics\Vibrio_cholerae.txt', 'r')
# MyBlock = f.read(100)
MyBlock = f.read()
# print(MyBlock)

textIn = MyBlock


patternIn = input('Enter pattern to count: ')
final_result = ''

result = patternCount(textIn, patternIn)
for i in result:
    final_result += str(i) + ' '
print(final_result)

f.close()








