def patternCount(text, pattern):
    count = 0
    patternlen = len(pattern)
    textlen = len(text)

    for i in range(0, textlen):
        patternInText = text[i:i + patternlen]  # slide window for text
        if text[i:i + patternlen] == pattern:
            count += 1

    return count  # Number of times pattern is in text

textIn = input('Enter text to scan:')
patternIn = input('Enter pattern to count:')
print('result:')
print(patternCount(textIn,patternIn))


