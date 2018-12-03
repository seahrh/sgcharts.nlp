__all__ = ['ngram_from_tokens_gen', 'ngram_gen']


def ngram_from_tokens_gen(tokens, n=1):
    """Generates ngrams from list of tokens.
    Each ngram is a tuple of tokens.
    """
    return zip(*[tokens[i:] for i in range(n)])


def ngram_gen(string, separator=' ', n=1):
    """Generates ngrams from a string."""
    return ngram_from_tokens_gen(string.split(separator), n=n)
