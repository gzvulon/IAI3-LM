from dataset_builder import DatasetBuilder
from agent_comparator import AgentComparator
import s_learning_curve_sttemming
import s_learning_curve_simple
import agent


def createTestDataset():
    '''
    @return: A test dataset.
    '''
    return [
        ('I love dogs.', True),
        ('I love cats.', True),
        ('I love children.', True),
        ('I love chicken.', True),
        ('I love being amused.', True),
        ('I like dogs.', True),
        ('I like cats.', True),
        ('I like children.', True),
        ('I like chicken.', True),
        ('I like being amused.', True),
        ('I hate slugs.', False),
        ('I hate mud.', False),
        ('I hate jerks.', False),
        ('I hate broccoli.', False),
        ('I hate being bored.', False),
        ('I dislike slugs.', False),
        ('I dislike mud.', False),
        ('I dislike jerks.', False),
        ('I dislike broccoli.', False),
        ('I dislike being bored.', False)]

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

def runExperiment(name, data, agent1_class, agent2_class, classification_time_limit, learning_time_limit):
    '''
    Runs the comparator with the given parameters and prints its output.
    '''
    confusion1, confusion2, mcnemar = AgentComparator().run(data, agent1_class, agent2_class, classification_time_limit, learning_time_limit, 0)
    print name
    print '======================================================='
    print confusion1
    print '======================================================='
    print confusion2
    print '======================================================='
    print mcnemar
    print '~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~'
    print 

Agent1 = agent.AgentCommonVerbs   #s_learning_curve_sttemming.MakeAgentClass(10)
Agent2 = s_learning_curve_simple.MakeAgentLimitedClass(10)


print "start"
# Real Data #
datasets = createRealDatasets()
for name, dataset in datasets.items():
    runExperiment(name, dataset, Agent1, Agent2, 2, 60)
