import os
import computing_frequencies
import number_to_pattern
import pattern_to_number
import tkinter as tk
from tkinter import filedialog


def better_clump_finding(genome_file_path, k, L, t):
    frequent_patterns = []
    clump = []

    genome_len = os.path.getsize(genome_file_path)
    f = open(genome_file_path, 'r')

    frequency_array = []
    pattern = ''
    for i in range(0, (4 ** k)):
        clump.append(0)
        print('appending 0, at i:' + str(i))

    text = f.read(L)
    frequency_array = computing_frequencies.computing_frequencies(text, k)
    for index in range(0, (4 ** k)):
        if frequency_array[index] >= t:
            clump[index] = 1
    f.seek(0, 0)
    for i in range(0, genome_len - L + 1):  # testing here...
        first_pattern = f.read(k)
        index = pattern_to_number.pattern_to_number(first_pattern)
        frequency_array[index] = frequency_array[index] - 1
        f.seek(i + L - k)
        last_pattern = f.read(k)
        index = pattern_to_number.pattern_to_number(last_pattern)
        frequency_array[index] = frequency_array[index] + 1
        if frequency_array[index] >= t:
            clump[index] = 1
        f.seek(i + 1)  # position for next read

    for i in range(0, (4 ** k)):
        if (clump[i] == 1):
            pattern = number_to_pattern.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    f.close()
    return frequent_patterns


genomeIn = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
kIn = 11
L_In = 547
tIn = 20
# 12 557 16



# result = clump_finding(genomeIn, kIn, L_In, tIn)

# print(result)



root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
# f = open(file_path, 'r')

result = better_clump_finding(file_path, kIn, L_In, tIn)
print(result)
print(result)
for item in result:
    print(item, end=' ')

