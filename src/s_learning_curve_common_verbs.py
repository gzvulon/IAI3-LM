#!/usr/bin/env python
'''
Created on Jun 23, 2011

@author: inesmeya
'''

from learning_agent import LearningAgent
from nearest_neighbor import NearestNeighbor
import s_learning_curve
from s_bag_of_words import BagOfWordsFiltered
import s_text_filter


def MakeAgentClass(n):
    class AgentLimited(LearningAgent):
        def createFeatureExtractor(self):
            return BagOfWordsFiltered(n, [s_text_filter.word_list_filter, 
                                          s_text_filter.suffix_stem, 
                                          s_text_filter.common_verbs_filter])
         
        def createClassifier(self):
            return NearestNeighbor()
        
        def __str__(self):
            return 'Agent_[common_verbs_filter]_' + str(n)
    return AgentLimited

def main():

    agentClassGenerator = MakeAgentClass
    s_learning_curve.main(agentClassGenerator)

if __name__ == '__main__':
    main()
