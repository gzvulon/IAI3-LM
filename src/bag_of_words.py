from feature_extractor import FeatureExtractor
import re
from numpy.ma.core import log

class BagOfWords(FeatureExtractor):
    '''
    Extracts a bag of words representation with TFIDF scores from raw text.
    '''
    
    def __init__(self, num_features):
        '''
        Constructor.
        
        @param num_features: The number of features to extract.
        '''
        self.num_features = num_features
    
    def extract(self, raw_instance):
        '''
        Creates a new instance in the feature-space from the given raw instance.
        
        @param raw_instance: A string.
        @return: A tuple of numerical features, each feature representing a word 
                 and its TFIDF score.
        '''
        tf = self._countTermFrequency(raw_instance)
        features = []
        for word in self.order:
            if word in tf:
                features += [tf[word] * self.idf[word]]
            else:
                features += [0]
        return tuple(features)
    
    def setup(self, examples, extraction_time_limit, setup_time_limit):
        '''
        Prepares a dictionary of inverse-document-frequencies (IDFs) for each word,
        and selects the terms with the highest IDFs as the features.
        
        @param examples: A list of raw data examples.
        @param extraction_time_limit: The time that will be allocated for each example.
        @param setup_time_limit: The time limit for setting up this agent.
        '''
        self.extraction_time_limit = extraction_time_limit
        
        doc_count = float(len(examples))
        tf_examples = []
        for raw_example in examples: 
            tf_examples += [self._countTermFrequency(raw_example)]
        self.idf = self._countInverseDocumentFrequency(tf_examples)
        
        self.order = sorted(self.idf.items(), lambda item1, item2: -cmp(item1[1], item2[1]))
        self.order = self.order[:self.num_features]
        self.idf = dict(self.order)
        self.order = [x[0] for x in self.order]
        
        for word in self.idf.keys():
            self.idf[word] = log(doc_count / self.idf[word])
    
    def _countTermFrequency(self, raw_example):
        '''
        Counts the frequency of each word in each document.
        
        @param raw_example: A raw example (strings).
        @return: A term frequency (word count) dictionary.
        '''
        example = {}
        total_count = 0
        for word in self._getTerms(raw_example):
            if word not in example:
                example[word] = 1.0
            else:
                example[word] += 1.0
            total_count += 1
        for word in example.keys():
            example[word] = example[word] / total_count
        return example
    
    def _countInverseDocumentFrequency(self, tf_examples):
        '''
        Counts the number of documents containing each word.
        
        @param tf_examples: A list of processed examples, each one represented by a term frequency 
                            (word count) dictionary.
        @return: A dictionary of each word and the number of different documents it appears in.
        '''
        idf = {}
        for example in tf_examples:
            for word in example.keys():
                if word not in idf:
                    idf[word] = 1
                else:
                    idf[word] += 1
        return idf
    
    def _getTerms(self, text):
        '''
        Retrieves all the terms (keywords) from the given text.
        This method defines a term to be an alphabetical string of at least three characters. 
        
        @param text: A string.
        @return: A list of terms.
        '''
        pattern = re.compile(r'[a-z]{3,}')
        return re.findall(pattern, text.lower())
