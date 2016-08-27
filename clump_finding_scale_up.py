import os
import computing_frequencies
import number_to_pattern
import tkinter as tk
from tkinter import filedialog


def clump_finding_scale_up(genome_file_path, k, L, t):

    frequent_patterns = []
    clump = []

    genome_len = os.path.getsize(genome_file_path)
    f = open(genome_file_path, 'r')

    frequency_array = []
    pattern = ''
    for i in range(0, (4 ** k)):
        clump.append(0)
        print('appending 0, at i:' + str(i))

    for i in range(0, genome_len - L + 1):  # testing here...
        # text = genome[i:i + L]
        text = f.read(L)
        frequency_array = computing_frequencies.computing_frequencies(text, k)
        f.seek(i + 1);
        for index in range(0, (4 ** k)):
            if frequency_array[index] >= t:
                clump[index] = 1
    for i in range(0, (4 ** k)):
        # if (clump[i] == 1) & (i < (L - 1)):
        if (clump[i] == 1):
            pattern = number_to_pattern.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    f.close()
    return frequent_patterns


genomeIn = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
kIn = 3
L_In = 25
tIn = 3

# result = clump_finding(genomeIn, kIn, L_In, tIn)

# print(result)



root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
# f = open(file_path, 'r')

result = clump_finding_scale_up(file_path, kIn, L_In, tIn)
print(result)

