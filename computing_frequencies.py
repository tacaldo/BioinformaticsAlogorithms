import pattern_to_number
def computing_frequencies(text, k):  #
    frequency_array = []
    pattern = ''
    last_pattern = ''
    text_len = len(text)
    for i in range(0, (4 ** k)):
        frequency_array.append(0)
    for i in range(0, text_len - k):
        pattern = text[i:k + i]
        j = pattern_to_number.pattern_to_number(pattern)
        frequency_array[j] += 1

    # last_pattern = text[i:i+k]
    last_pattern = text[text_len - k : text_len +1]

    # last_pattern = text[i + 1:i + k]

    j = pattern_to_number.pattern_to_number(last_pattern)
    frequency_array[j] += 1

    return frequency_array


# print(computing_frequencies('TTAAA', 2))
# print(computing_frequencies('AAAAC', 2))
# print(computing_frequencies('AAA', 2))

# result = computing_frequencies('TTAAATCATTTTCCAGTACGCACGCGGATCGCCAGGTGGGGTAAGGTACTCTTGGTACATGAAAGGGTATAGTTCCGCGCGCAACGCGGCAGCAGTTTCAAACTGCTGATTATCGTTGGTACGCCACCGACGTCCCGTAGTCGTTTCTCAGCTCTTGTTGCATCGCTCGTAACTATGTAGCAGACGGCGTCCGGAACGAACAACTTTTTTCGATAGAACTCCTCGCAGGTCTCGCGCATGGCGCTACCTTGTGTCTACCTGGAGGGGACCACAACTAATACCATCGGGAAGTGGGCTATCCGCTCGAAGTTTAGACTGCGGTCACAACGGGCTTCCGGACGAGGTATCGCGGTTCCGACACTTGATATAACGGAGCTACGGTGATCTTCCGTTGGCGTCTATTCAGAACAGCGGCAAGGCGGTATAGTCGAACCTCCTCATCCAAAAATTTCCCTGCCCGTCCCCATGGTCTGTTACCCAACCGTCGATTCGTGCATGGCGAGTGACGCGGCTGCACGACAATCAAAGACACAGATAATTTCGTACTGGCCTCCACAGGTACGGCGGTCTATCAGATCCTTAATCAGGTGTGATGCTGACTCAAATGCTAAGTGTTCACACATACGCGCAGACTGAGTACGTTTCACCCCTATAGTGTATTTGAGTTATAGAGTGTGCTGCACTGTCTAAAGTCTTCACAGTAAGTGTTTGCCACTGAGATCTACAAATGTTTGCCATAGTATCGCTTTTACGGTTTAGGGTACAATACTCACTCTCAAGTATGTCCTACTAT', 5)
#
# final_result = ''
#
# for i in result:
#     final_result += str(i) + ' '
#
# print('\n\nfinal result is: ' + final_result)




# print(computing_frequencies('ACTTCGCCTAAGTCATTTATCCCGTGGTACGACGCTCCCTTACAGTCTTATATCCCGGTATATACGCAGAAATGCCTACGTCCCCTCGTCCCACACACCAGGGAAGCTGAAATCGCTCATCTACTATGCGTGTACTTCCGGACGAAATCGTCGTCGGCTTCTGTCTGGCGCTGGAGATCCGGGCTTCTTGAGGGACACACCCATTATGACCGTTACAGGACTTACAACTACTCTGAGCAATGATGGTGCTCTGTAACGAACAAACGCACTCACCTCTGTTTCCTGTATGACATCCTCAAATGGATCGACCGTGATGTACTGAGCGAATAAGTGCGGATTACATTTATAGTCAGCTACATTTATTCGCCGCTCGGAGCAGAGTATAATGAATTTATACCACTTGTTAGACTCCTTCTCGCATTTAGCCCCTACCGCAAGTCGGAGCGTTGGGGTGCAATAGAGTTTTCAGTATCTACGTACCGTTAAGTCTCTCGCGTTCTTTCAGCAGGCATCAATATGTTGCTTGCTGTGGGGTCGGGTGGGGCGGAGAGCCAATAAAGTGCATCGGAATTGGCTGCCCTCCTACGAATCCGCAAGATGCGGTGATGCTACGTGATTATGACTACTAGCTTAGTCCC', 6))

