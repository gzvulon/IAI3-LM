#!/usr/bin/env python
'''
Created on Jun 23, 2011

@author: inesmeya
'''

from learning_agent import LearningAgent
from nearest_neighbor import NearestNeighbor
from s_bag_of_words import BagOfWordsFiltered
import s_text_filter

BAG_SIZE =10

# this code is taken from s_learning_curve_common_verbs.py
class AgentCommonVerbs(LearningAgent):
    def createFeatureExtractor(self):
        return BagOfWordsFiltered(BAG_SIZE, [s_text_filter.word_list_filter, 
                                      s_text_filter.suffix_stem, 
                                      s_text_filter.common_verbs_filter])
    def createClassifier(self):
        return NearestNeighbor()
    
    def __str__(self):
        return 'Agent_[common_verbs_filter]_' + str(BAG_SIZE)