'''
Created on Jun 23, 2011

@author: hizki
'''
import unittest
from distutils import text_file
import s_i_filters
from s_i_filters import word_filter
from test_steam import the_text


class Test(unittest.TestCase):


    def setUp(self):
        pass


    def tearDown(self):
        pass


    def test_suffix_stem_simple_examples(self):
        terms = ['sses', 'ies', 'ss', 's', 'meed', 'ed', 'ing', 'at', 'bl', 'iz']
        fixed_terms = s_i_filters.suffix_stem(terms)
        self.assertEqual(fixed_terms, ['ss', 'i', 'ss', '', 'mee', '', '', 'ate', 'ble', 'ize'])

    def test_suffix_stem_complex_example1(self):
        terms = ['ssesessses']
        self.assertEqual(s_i_filters.suffix_stem(terms), ['ssesesss'])
    
    def test_suffix_stem_complex_example2(self):
        terms = ['ssesessss']
        self.assertEqual(s_i_filters.suffix_stem(terms), ['ssesessss'])

    def test_suffix_stem_complex_example3(self):
        terms = ['eeesseseed']
        self.assertEqual(s_i_filters.suffix_stem(terms), ['eeessesee'])
        
    def test_suffix_stem_complex_example4(self):
        terms = ['inging']
        self.assertEqual(s_i_filters.suffix_stem(terms), ['ing'])
    
    def test_size(self):
        terms = word_filter(the_text)
        terms1 = s_i_filters.suffix_stem(terms)
        self.assertEqual(len(terms), len(terms1))

    
        

            



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testSuffix_stem']
    unittest.main()