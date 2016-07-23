import frequent_words

textIn = input('Enter text to scan: ')
kIn = int(input('Enter k-mer size (int): '))
print('\nworking with string of size: ' + str(len(textIn)) + '\n')

output = frequent_words.get_frequent_words(textIn,kIn)


print(output)





