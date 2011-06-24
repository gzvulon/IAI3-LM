import scp
from s_agent_comparor import AgentComparator
import s_learning_curve_simple
import s_learning_curve_black_list
import s_learning_curve_sttemming
import s_learning_curve_both_back_stemming

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


def main_measure(datasets, (agent1_class, agent2_class),params):
    
    NUM_FOLDS       = params[scp.NUM_FOLDS]
    CLASSIFY_TIME   = params[scp.CLASSIFY_TIME]
    LEARN_TIME      = params[scp.LEARN_TIME]
    
    print "\n============= Paired Test ==================="
    a1_name = str(agent1_class())
    a2_name = str(agent2_class())
    
    print "%s vs  %s" % (a1_name,a2_name)
    print "------------------------------"
    print "dataset, %s significance, %s accuracy, %s  accuracy" % (a1_name,a1_name,a2_name)


    results_mes = []
    
    for data_name, dataset in datasets.items():
        try:
            gc.disable()
            confusion1, confusion2, mcnemar = AgentComparator().run(dataset, agent1_class, agent2_class, CLASSIFY_TIME, LEARN_TIME, NUM_FOLDS)
            gc.enable()
            gc.collect()
            
            res = (data_name, mcnemar.getFirstSignStr(), confusion1.getAccuracyStr(), confusion2.getAccuracyStr() )
            for r in res: print r,',',
            print
            
            res = (data_name, mcnemar, confusion1, confusion2 )
            results_mes.append(res)
            
        except:
            print "Timeout for", data_name
        
    return results_mes



def print_mres(mres):
    for res in mres:
        print "############################"
        for e in res: print e
        

def main(agentClassPairs):
    params = {
        scp.X_POINTS : 20, #not relevat
        scp.STEP :     5, #not relevat
        scp.NUM_FOLDS : 0,
        scp.CLASSIFY_TIME : 2,
        scp.LEARN_TIME : 60*2,
        scp.SEED : 1
    }
    
    N = 10
    
    datasets = createRealDatasets()
    print " ~~~~~~~~~~ Paired Tests ~~~~~~~~~~~"
    print " vector size=", N
    print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
    print
    
    results = []
    
    for pair in agentClassPairs:
        res = main_measure(datasets, pair, params)
        results.append(res)
        
    print "\n=================== Detatils:"
    
    for r in results:
        print_mres(r)
        
    
    





if __name__ == '__main__':
    main()