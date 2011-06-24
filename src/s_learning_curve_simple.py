#!/usr/bin/env python
'''
Created on Jun 23, 2011

@author: inesmeya
'''

from learning_agent import LearningAgent
from bag_of_words import BagOfWords
from nearest_neighbor import NearestNeighbor
import s_learning_curve


def MakeAgentLimitedClass(n):
    class AgentLimited(LearningAgent):
        def createFeatureExtractor(self):
            return BagOfWords(n)
        
        def createClassifier(self):
            return NearestNeighbor()
        
        def __str__(self):
            return 'AgentLimited_' + str(n)
    return AgentLimited

def main():

    agentClassGenerator = MakeAgentLimitedClass
    s_learning_curve.main(agentClassGenerator)

if __name__ == '__main__':
    main()