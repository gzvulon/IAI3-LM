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