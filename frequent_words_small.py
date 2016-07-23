def patternCount(text, pattern):
    count = 0
    patternlen = len(pattern)
    textlen = len(text)

    for i in range(0, textlen):
        patternInText = text[i:i + patternlen]  # slide window for text
        if text[i:i + patternlen] == pattern:
            count += 1

    return count  # Number of times pattern is in text


def frequentWords(text, k):  # finds most frequent k-mers, most frequent k length patterns
    frequentPatterns = []
    pattern = ''
    count = []
    for i in range(0, len(text) - k):
        pattern = text[i:i + k]
        count.append(patternCount(text, pattern))
        print('adding pattern: ' + pattern + ' to count..')

    maxcount = max(count)  # more to do here
    for i in range(0, len(text) - k):
        if count[i] == maxcount:
            frequentPatterns.append(text[i:i + k])
            print(text[i:i + k])

    return set(frequentPatterns)  # set will get rid of duplicates in this case


textIn = input('Enter text to scan: ')
kIn = input('Enter k-mer size (int): ')
print('\nworking with string of size: ' + str(len(textIn)) + '\n')
myresult = frequentWords(textIn, int(kIn))
print(myresult)
