import re
import s_common_verbs

gRules = [
 ('sses', 'ss'),
 ('ies', 'i'),
 ('ss', 'ss'),
 ('s', ''),
 ('eed', 'ee'),
 ('ed', ''),
 ('ing', ''),
 ('at', 'ate'),
 ('bl', 'ble'),
 ('iz', 'ize')
 ]

def stem_word(word):
    if word == 'eed':
        return word
    
    for rule in gRules:
        suffix, exchange = rule
        suf_len = len(suffix)
        #skip if less than suffix
        if len(word) < suf_len: continue
        #change suffix if match
        if word[-suf_len:] == suffix:
            res = word[:-suf_len] + exchange
            return res
    return word

def suffix_stem(terms):
    '''
    Receives a list of terms and removes/changes their suffixes 
    as described in 1.a of the exercise. 
    
    @param terms: A list of terms (strings).
    @return: A list of terms with "fixed" suffixes.
    '''
    res = map(stem_word, terms)
    return res

def word_filter(text):
        pattern = re.compile(r'[a-z]{3,}')
        terms = re.findall(pattern, text.lower())
        return terms

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

def common_verbs_filter(terms):
    '''
    Removes all the terms that are in the list of 330 common English verbs.
    Note: We assume suffix_stem was applied to all the verbs are in their normal form.
    '''
    common_verbs = s_common_verbs.common_verbs
    res = filter(lambda term: not term in common_verbs, terms)
    return res