# -*- coding:utf-8 -*-
"""
Created on Jun 23, 2011

@author: inesmeya
"""
from numpy.ma.core import log

def idf(num_folds,data, num_of_features):
    ''' calculates idf using params:
    @param num_folds: number of folds as sent to agent
    @param data: data snt to agent
    @param num_of_features: number of features of bag of words
    '''
    if num_folds < 2:
        num_folds = len(data)
    
    fold_size = len(data) / num_folds
    doc_count = len(data) - fold_size
    idf = log(float(doc_count) / num_of_features)
    return idf


def test_idf():
    a,b = idf(0, [1,2,3,4], 2),  log(3.0/2)
    print a,b
    assert a == b
    
    
    a,b = idf(5, [1,2,3,4,5,6,7,8,9,10], 4),  log(8.0/4)
    print a,b 
    assert a == b

if __name__ == '__main__':
    test_idf()