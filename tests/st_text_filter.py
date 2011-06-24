'''
Created on Jun 23, 2011

@author: hizki
'''
import unittest
from distutils import text_file
import s_text_filter
<<<<<<< HEAD
import re
=======
from test_steam import the_text
from s_i_filters import word_filter
>>>>>>> 135b0600fd8d5b9eed0d0bfe1280d4d43656b3d1


class Test(unittest.TestCase):

    
    def setUp(self):
        self.word_pattern = re.compile(r'[a-z]{3,}')


    def tearDown(self):
        pass


    def test_suffix_stem_simple_examples(self):
        terms = ['sses', 'ies', 'ss', 's', 'meed', 'ed', 'ing', 'at', 'bl', 'iz']
        fixed_terms = s_text_filter.suffix_stem(terms)
        self.assertEqual(fixed_terms, ['ss', 'i', 'ss', '', 'mee', '', '', 'ate', 'ble', 'ize'])

    def test_suffix_stem_complex_example1(self):
        terms = ['ssesessses']
        self.assertEqual(s_text_filter.suffix_stem(terms), ['ssesesss'])
    
    def test_suffix_stem_complex_example2(self):
        terms = ['ssesessss']
        self.assertEqual(s_text_filter.suffix_stem(terms), ['ssesessss'])

    def test_suffix_stem_complex_example3(self):
        terms = ['eeesseseed']
        self.assertEqual(s_text_filter.suffix_stem(terms), ['eeessesee'])
        
    def test_suffix_stem_complex_example4(self):
        terms = ['inging']
        self.assertEqual(s_text_filter.suffix_stem(terms), ['ing'])
    
    def test_size(self):
        terms = word_filter(the_text)
        terms1 = s_text_filter.suffix_stem(terms)
        self.assertEqual(len(terms), len(terms1))

#    def test_suffix_stem_dont_lose_words(self):
#        terms = re.findall(self.word_pattern, text.lower())
#        for f in self.filter_func_list:
#            terms = f(terms)

    def test_word_list_filter1(self):
        print '== test_word_list_filter1 =='
        terms = ["dsfkj", 'sdw', 'a', "dff", 'on']
        res = s_text_filter.word_list_filter(terms)
        print res
        assert res== ["dsfkj", 'sdw',  "dff"]
    
        black_list = ["a", "an", "and", "are", "as", "at", "be", "but", "by", 
                  "for", "if", "in", "into", "is", "it", "no", "not", "of", 
                  "on", "or", "such", "that", "the", "their", "then", "there", 
                  "these", "they", "this", "to", "was", "will", "with"]
        res = s_text_filter.word_list_filter(black_list)
        print "empty:" , res
        assert res == []
    
    def test_filtering(self):
        filter_func_list = [s_text_filter.word_list_filter, s_text_filter.suffix_stem]
        terms = ['and', 'anded', 'gess', 'dsfdf']
        for f in filter_func_list:
            terms = f(terms)
        print "test_filtering"
        print terms
            



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSuffix_stem']
    unittest.main()