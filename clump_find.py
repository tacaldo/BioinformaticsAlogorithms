import frequent_words

def clump_find(genome, k, L, t):
    """integers L and t,a k-mer Pattern forms an (L,t)-clump inside
    a(longer) string Genome if there is an interval of Genome of length L in which
    this k-mer appears at least t times, k-mer must fit within the interval"""

    output = frequent_words.get_frequent_words(genome[0:L],k)


    return
