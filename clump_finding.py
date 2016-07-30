import computing_frequencies
import number_to_pattern


def clump_finding(genome, k, t, L):
    frequent_patterns = []
    clump = []
    genome_len = len(genome)
    frequency_array = []
    pattern = ''
    for i in range(0, (4 ** k)):
        clump.append(0)
    for i in range(0, genome_len - L):
        text = genome[i:i + L]
        frequency_array = computing_frequencies.computing_frequencies(text, k)
        for index in range(0, (4 ** k)):
            if frequency_array[index] >= t:
                clump[index] = 1
    for i in range(0, (4 ** k)):
        if clump[i] == 1:
            pattern = number_to_pattern.number_to_pattern(i, k)
            frequent_patterns.append(pattern)

    return frequent_patterns
