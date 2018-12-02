__all__ = ['tok']

from .util import compile_infix_regex, compile_prefix_regex, compile_suffix_regex
from .punctuation import TOKENIZER_INFIXES, TOKENIZER_PREFIXES, TOKENIZER_SUFFIXES
from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS

__prefixes = tuple(TOKENIZER_PREFIXES)
__suffixes = tuple(TOKENIZER_SUFFIXES)
__infixes = tuple(TOKENIZER_INFIXES)
__prefix_search = (compile_prefix_regex(__prefixes).search if __prefixes else None)
__suffix_search = (compile_suffix_regex(__suffixes).search if __suffixes else None)
__infix_finditer = (compile_infix_regex(__infixes).finditer if __infixes else None)


def __find_prefix(string):
    """Find the length of a prefix that should be segmented from the
            string, or None if no prefix rules match.
            string (unicode): The string to segment.
            RETURNS (int): The length of the prefix if present, otherwise `None`.
            """
    if __prefix_search is None:
        return 0
    match = __prefix_search(string)
    return (match.end() - match.start()) if match is not None else 0


def __find_suffix(string):
    """Find the length of a suffix that should be segmented from the
    string, or None if no suffix rules match.
    string (unicode): The string to segment.
    Returns (int): The length of the suffix if present, otherwise `None`.
    """
    if __suffix_search is None:
        return 0
    match = __suffix_search(string)
    return (match.end() - match.start()) if match is not None else 0


def __find_infix(string):
    """Find internal split points of the string, such as hyphens.
    string (unicode): The string to segment.
    RETURNS (list): A list of `re.MatchObject` objects that have `.start()`
        and `.end()` methods, denoting the placement of internal segment
        separators, e.g. hyphens.
    """
    res = []
    if __infix_finditer is not None:
        res.extend(list(__infix_finditer(string)))
    return res


def tok(text, special_cases=TOKENIZER_EXCEPTIONS, find_prefix=__find_prefix, find_suffix=__find_suffix,
        find_infixes=__find_infix):
    tokens = []
    for substring in text.split(' '):
        suffixes = []
        while substring:
            if special_cases is not None and substring in special_cases:
                tokens.extend(special_cases[substring])
                substring = ''
                continue
            split = find_prefix(substring)
            if split != 0:
                tokens.append(substring[:split])
                substring = substring[split:]
                continue
            split = find_suffix(substring)
            if split != 0:
                suffixes.append(substring[-split:])
                substring = substring[:-split]
                continue
            infixes = find_infixes(substring)
            if len(infixes) != 0:
                offset = 0
                for match in infixes:
                    tokens.append(substring[offset:match.start()])
                    tokens.append(substring[match.start():match.end()])
                    offset = match.end()
                substring = substring[offset:]
                continue
            tokens.append(substring)
            substring = ''
        tokens.extend(reversed(suffixes))
    return tokens
