# -*- coding:utf-8 -*-
"""
Created on Jun 23, 2011

@author: inesmeya
"""
from dataset_builder import DatasetBuilder
from nearest_neighbor import NearestNeighbor
from bag_of_words import BagOfWords
from learning_agent import LearningAgent
from s_agent_comparor import AgentComparator

def createRealDatasets(dir = 'topics/'):
    '''
    @return: A dictionary of the real datasets, with their names as keys.
    '''
    builder = DatasetBuilder()
    datasets = {}
    datasets['Windows 7: Features or speed?'] = builder.fromFiles([dir+'features_windows7.txt.data', dir+'speed_windows7.txt.data'])
    datasets['Best Western Hotels: Bath or room?'] = builder.fromFiles([dir+'bathroom_bestwestern_hotel_sfo.txt.data', dir+'rooms_bestwestern_hotel_sfo.txt.data'])
    datasets['Hotels: San Francisco or Chicago?'] = builder.fromFiles([dir+'rooms_bestwestern_hotel_sfo.txt.data', dir+'rooms_swissotel_chicago.txt.data'])
    datasets['Battery life: Which device?'] = builder.fromFiles([dir+'battery-life_amazon_kindle.txt.data', dir+'battery-life_ipod_nano_8gb.txt.data', dir+'battery-life_netbook_1005ha.txt.data'])
    datasets['iPod Nano: Which aspect?'] = builder.fromFiles([dir+'battery-life_ipod_nano_8gb.txt.data', dir+'screen_ipod_nano_8gb.txt.data', dir+'sound_ipod_nano_8gb.txt.data', dir+'video_ipod_nano_8gb.txt.data'])
    return datasets



def MakeAgentLimitedClass(n):
    class AgentLimited(LearningAgent):
        def createFeatureExtractor(self):
            return BagOfWords(n)
        
        def createClassifier(self):
            return NearestNeighbor()
        
        def __str__(self):
            return 'AgentLimited_' + str(n)
    return AgentLimited



def print_results(results,dataname):
    print "============= Learning Curve ==================="
    print " -- ", dataname, "--"
    for num_features,confusion in results:
        print num_features, '%.2f%' % (confusion.getAccuracy()*100)

def main_measure(data, dataname):
    N = 20
    STEP = 5
    num_features_arr =  [ i*STEP for i in range(1,N +1) ]
    print "Evaluating", dataname
    results=[]
    for num_features in num_features_arr:
        agentClass = MakeAgentLimitedClass(num_features)
        confusion = AgentComparator().run_one(data, agentClass, 10, 300, num_folds=10, seed=1)
        results.append( (num_features,confusion) )
        print "num_features:",num_features," => ", 'Accuracy: %.2f%%' % (confusion.getAccuracy()*100)
    print_results(results,dataname)
    

def main():
    datasets = createRealDatasets()
    for name, dataset in datasets.items():
        main_measure(dataset,name)



main()        

