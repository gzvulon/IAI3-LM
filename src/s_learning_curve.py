# -*- coding:utf-8 -*-
"""
Created on Jun 23, 2011

@author: inesmeya
"""
from dataset_builder import DatasetBuilder
import scp
import s_common
import gc
from s_learning_analyzer import AgentAnalyzer

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


def main_measure(data, dataname,agentClassGenerator,params):
    
    X_POINTS        = params[scp.X_POINTS]
    STEP            = params[scp.STEP]
    NUM_FOLDS       = params[scp.NUM_FOLDS]
    CLASSIFY_TIME   = params[scp.CLASSIFY_TIME]
    LEARN_TIME      = params[scp.LEARN_TIME]
    SEED            = params[scp.SEED]
    
    num_features_arr =  [ i*STEP for i in range(1,X_POINTS +1) ]
    print "\n============= Learning Curve ==================="
    print "Evaluating", dataname
    print "num_features,", "accuracy%,"
     
    results=[]
    for num_features in num_features_arr:
        agentClass = agentClassGenerator(num_features)
        
        try:
            gc.disable()
            confusion = AgentAnalyzer().run_one(data, agentClass, CLASSIFY_TIME, LEARN_TIME, num_folds=NUM_FOLDS, seed=SEED)
            gc.enable()
            gc.collect()
            
            idf = s_common.idf(NUM_FOLDS, data, num_features)
            results.append( (num_features,confusion, idf) )
            print num_features, ',', confusion.getAccuracyStr()
        
        except Exception, e:
            print "Error:",e
            print " Possible Timeout for", num_features

def main_old(agentClassGenerator, params):
    '''
    @param agentClassGenerator:  fn: int <number of features> --> AgentClass
    @param params: example:
    {
        'X_POINTS' : 3,
        'STEP' : 5,
        'NUM_FOLDS' : 10,
        'CLASSIFY_TIME' : 5,
        'LEARN_TIME' : 30,
        'SEED' : 1
    }
    '''
    datasets = createRealDatasets()
    for name, dataset in datasets.items():
        main_measure(dataset,name,agentClassGenerator,params)

def main(agentClassGenerator):
    main_old(agentClassGenerator, scp.params_to_100)
    print
    print "#####################################"
    print
    main_old(agentClassGenerator, scp.params_to_20)


