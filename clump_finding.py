import computing_frequencies
import number_to_pattern


def clump_finding(genome, k, L, t):
    """integers L and t,a k-mer Pattern forms an (L,t)-clump inside
        a (longer) string Genome if there is an interval of Genome of length L in which
        this k-mer appears at least t times, k-mer must fit within the interval"""
    frequent_patterns = []
    clump = []
    genome_len = len(genome)
    frequency_array = []
    pattern = ''
    for i in range(0, (4 ** k)):
        clump.append(0)
    for i in range(0, genome_len - L + 1): # testing here...
        text = genome[i:i + L]
        frequency_array = computing_frequencies.computing_frequencies(text, k)
        for index in range(0, (4 ** k)):
            if frequency_array[index] >= t:
                clump[index] = 1
    for i in range(0, (4 ** k)):
        # if (clump[i] == 1) & (i < (L - 1)):
        if (clump[i] == 1):
            pattern = number_to_pattern.number_to_pattern(i, k)
            frequent_patterns.append(pattern)
    return frequent_patterns

genomeIn = 'CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG'
kIn = 3
L_In = 25
tIn = 3

result = clump_finding(genomeIn, kIn, L_In, tIn)

print(result)
