import re

def suffix_stem(terms):
    '''
    Receives a list of terms and removes/changes their suffixes 
    as described in 1.a of the exercise. 
    
    @param terms: A list of terms (strings).
    @return: A list of terms with "fixed" suffixes.
    '''
    fixed_terms = []
    suffixes = [(r'[a-z]*sses$', 4, 'ss'),(r'[a-z]*ies$', 3, 'i'),(r'[a-z]*ss$', 2, 'ss'),
                (r'[a-z]*s$', 1, ''),(r'[a-z]+eed$', 3, 'ee'),(r'[a-z]*ed$', 2, ''),
                (r'[a-z]*ing$', 3, ''), (r'[a-z]*at$', 2, 'ate'),(r'[a-z]*bl$', 2, 'ble'),
                (r'[a-z]*iz$', 2, 'ize')]
    
    for term in terms:
        for reg, cut, new_suffix in suffixes:
            if re.match(reg, term):
                fixed_terms.append(term[:-cut]+new_suffix)
                break
    
    return fixed_terms


def word_list_filter(terms):
    '''
    @param terms: list of words
    
    '''
    black_list = ["a", "an", "and", "are", "as", "at", "be", "but", "by", 
                  "for", "if", "in", "into", "is", "it", "no", "not", "of", 
                  "on", "or", "such", "that", "the", "their", "then", "there", 
                  "these", "they", "this", "to", "was", "will", "with"]
    res = filter(lambda term: not term in black_list, terms)
    return res