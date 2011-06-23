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
                      

    
def test_word_list_filter1():
    print '== test_word_list_filter1 =='
    terms = ["dsfkj", 'sdw', 'a', "dff", 'on']
    res = word_list_filter(terms)
    print res
    assert res== ["dsfkj", 'sdw',  "dff"]

    black_list = ["a", "an", "and", "are", "as", "at", "be", "but", "by", 
              "for", "if", "in", "into", "is", "it", "no", "not", "of", 
              "on", "or", "such", "that", "the", "their", "then", "there", 
              "these", "they", "this", "to", "was", "will", "with"]
    res = word_list_filter(black_list)
    print "empty:" , res
    assert res == []
    
    print word_list_filter(word_filter(the_text))
        
test_word_list_filter1()                