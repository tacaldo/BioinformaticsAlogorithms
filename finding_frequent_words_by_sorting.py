import pattern_to_number
import number_to_pattern


def finding_frequent_words_by_sorting(text, k):
    frequent_patterns = []
    index = []
    count = []
    sorted_index = []
    text_len = len(text)
    max_count = 0
    for i in range(0, text_len - k):
        pattern = text[i:k + 1]
        index.append(pattern_to_number.pattern_to_number(pattern))
        count.append(1)

    index.sort()
    sorted_index = index[:]

    for i in range(1, text_len - k):
        if sorted_index[i] == sorted_index[i - 1]:
            count[i] = count[i - 1] + 1
        max_count = max(count)
    for i in range(0, text_len - k):
        if count[i] == max_count:
            pattern = number_to_pattern.number_to_pattern(sorted_index[i], k)
            frequent_patterns.append(pattern)
    return frequent_patterns

text = 'ACTCACTTACTCATACTG'
k = 4

print (finding_frequent_words_by_sorting(text,k))



