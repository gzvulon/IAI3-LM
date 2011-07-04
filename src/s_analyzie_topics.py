# -*- coding:utf-8 -*-
"""
Created on Jun 24, 2011

@author: inesmeya
"""
import re
import s_text_filter


class DatasetBuilder:
    '''
    Builds a dataset from text files.
    '''
    
    def fromFiles(self, paths):
        '''
        @param path: A list of paths.
        @return: A list of (instance, classification) tuples. 
                 Each instance is a string.
        '''
        data = []
        for path in paths:
            f = open(path)
            classification = f.name[(f.name.rindex('/') + 1):f.name.index('.')]
            for line in f.readlines():
                data += [(line.strip(), classification)]
        return data
    

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
    



def line_to_words(line):
    pattern = re.compile(r'[a-z]{3,}')
    terms = re.findall(pattern, line.lower()) 
    return terms



def dataStatFileter(name,data, filter_list):
    zmin = 100000
    zmax = -1
    zsum = 0
    zcount = 0 
    lr = []

    for line, _ in data:
        terms = line_to_words(line)
        
        for f in filter_list:
            terms = f(terms)
        
        len_terms = len(terms)
        
        lr.append(len_terms)
        
        zmin = min(len_terms, zmin)
        zmax = max(len_terms, zmax)
        zsum += len_terms
        zcount +=1
    lr = sorted(lr)
    zmed = lr[len(lr)/2]
    print  "%10s, %4s, %4s, %.2f, %4s" % ( name, zmin, zmax, float(zsum)/zcount, zmed)
    
def dataStat(data):
    
    print "%10s, %4s, %4s, %4s, %4s" % ("filter","Min", "Max", "Avg", "Med")
    dataStatFileter("simple", data,[ ] )
    dataStatFileter("black word", data, [s_text_filter.word_list_filter])
    dataStatFileter("verbs_r",data, [s_text_filter.word_list_filter, s_text_filter.suffix_stem,s_text_filter.common_verbs_filter ],)
    

        
        


def wordsInLine():
    dss = createRealDatasets()
    for name, data in dss.items():
        print "DS:", name
        dataStat(data)
        print


def uniqeWordsInDatasetE():               
    dss = createRealDatasets()
    
    print "===========uniqeWordsInDataset================="
    for name, data in dss.items(): 
        print "DS:", name 
        uniqeWordsInDataset("simple", data,[ ] )
        uniqeWordsInDataset("black word", data, [s_text_filter.word_list_filter])
        uniqeWordsInDataset("verbs_r",data, [s_text_filter.word_list_filter, s_text_filter.suffix_stem,s_text_filter.common_verbs_filter ],)
        print
              
def uniqeWordsInDataset(name,data, flist):

        s = set()
               
        for line, _ in data:
            terms = line_to_words(line)
            for f in flist:
                terms = f(terms) 
            s.update(set(terms))
        print name,",", len(s)
wordsInLine()        
uniqeWordsInDatasetE()    
    
    
    
    
    
    
    