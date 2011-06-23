import re

def suffix_stem(terms):
    '''
    Receives a list of terms and removes/changes their suffixes 
    as described in 1.a of the exercise. 
    
    @param terms: A list of terms (strings).
    @return: A list of terms with "fixed" suffixes.
    '''
    fixed_terms = []
    suffixes = [(r'[a-z]*sses', 4, 'ss'),(r'[a-z]*ies', 3, 'i'),(r'[a-z]*ss', 2, 'ss'),
                (r'[a-z]*s', 1, ''),(r'[a-z]+eed', 3, 'ee'),(r'ed', 2, ''),(r'ing', 3, ''),
                (r'at', 2, 'ate'),(r'bl', 2, 'ble'),(r'iz', 2, 'ize')]
    
    for term in terms:
        for suffix, cut, new_suffix in suffixes:
            if re.match(term, suffix):
                fixed_terms.append(term[:-cut]+new_suffix)
                break
        