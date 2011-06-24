# -*- coding:utf-8 -*-
"""
Created on Jun 23, 2011

@author: inesmeya
"""
import re

the_text = 'A week ago, I ordered my Kindle 2 and when it was delivered, the battery was in critical stage and it would not power on .'

def word_filter(text):
        pattern = re.compile(r'[a-z]{3,}')
        terms = re.findall(pattern, text.lower())
        return terms
    
def test_word_filter():
        print '== test_word_filter =='
        res = word_filter(the_text)
        assert res == ['week', 'ago', 'ordered', 'kindle', 'and', 'when', 'was', 'delivered', 'the', 'battery', 'was', 'critical', 'stage', 'and', 'would', 'not', 'power']
        for r in res: print r
        print

''' ======================  Steam Implementation ======================='''

            #1) SSES → SS
            #2) IES → I
            #3) SS → SS
            #4) S → NULL
            #5) (m>0) EED → EE (m is the number of letters before EED)
            #6) ED → NULL
            #7) ING → NULL
            #8) AT → ATE
            #9) BL → BLE
            #10) IZ → IZE
            #Important note: For each word,      
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
    res = map(stem_word, terms)
    return res 
