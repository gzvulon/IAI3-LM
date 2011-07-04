# -*- coding:utf-8 -*-
"""
Created on Jun 24, 2011

@author: inesmeya
"""
from s_bag_of_words import BagOfWordsFiltered
import s_text_filter

def test_bag():
    bag = BagOfWordsFiltered(10, [s_text_filter.word_list_filter, 
                                          s_text_filter.suffix_stem])
    text = "once upon a time we indeed went to those gorgioes appartment on the beach and walking"
    ['once', 'upon', 'time', 'indee', 'went', 'those', 'gorgioe', 'appartment', 'beach', 'walk']
    terms = bag._getTerms(text)
    print terms
    
test_bag()