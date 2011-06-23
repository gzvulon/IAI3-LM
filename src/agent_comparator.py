from scipy.stats import binom_test
import time
from random import Random

class AgentComparator:
    '''
    Compares two learning agents by cross-validation and 
    McNemar's test for statistical significance.
    '''
    
    def run(self, data, agent1_class, agent2_class, classification_time_limit, learning_time_limit, num_folds = 0, seed = 1):
        '''
        Compares two learning agents by cross-validation of the 
        given dataset and McNemar's test for statistical significance.
        
        @param data: A list of examples and their classification. Assumes the class is discrete.
        @param agent1_class: The first agent's class. 
        @param agent2_class: The second agent's class.
        @param classification_time_limit: The time limit for classification of a single instance.
        @param learning_time_limit: The time limit for learning.
        @param num_folds: The number of folds to perform cross validation upon.
        @param seed: The random generator's seed for creating the folds.
        @return: The tuple (confusion1, confusion2, mcnemar).
                 confusion1 - The first agent's confusion matrix.
                 confusion2 - The second agent's confusion matrix.
                 mcnemar    - McNemar's comparison of the agents.
        '''
        classes = tuple(set(instance[1] for instance in data))
        confusion1 = ConfusionMatrix(classes)
        confusion2 = ConfusionMatrix(classes)
        mcnemar = McNemarMatrix(str(agent1_class()), str(agent2_class()))
        
        shuffled_data = data[:]
        rnd = Random(seed)
        rnd.shuffle(shuffled_data)
        
        for train, test in self._createFolds(shuffled_data, num_folds):
            agent1 = self._setupAgent(train, agent1_class, classification_time_limit, learning_time_limit)
            agent2 = self._setupAgent(train, agent2_class, classification_time_limit, learning_time_limit)
            
            for test_instance, test_classification in test:
                classification1 = self._classify(test_instance, agent1, classification_time_limit)
                classification2 = self._classify(test_instance, agent2, classification_time_limit)
                
                confusion1.update(test_classification, classification1)
                confusion2.update(test_classification, classification2)
                mcnemar.update(test_classification == classification1, test_classification == classification2)
        
        return (confusion1, confusion2, mcnemar)
    
    def _createFolds(self, data, num_folds):
        '''
        Creates the cross-validation folds.
        
        @param data: The original dataset, shuffled.
        @param num_folds: The number of folds to create. If this parameter is less than zero, leave-one-out will be used instead.
        @return: A list of (train, test) folds.
        '''
        if num_folds < 2:
            num_folds = len(data)
        
        fold_size = len(data) / num_folds
        remainder = len(data) % num_folds
        
        folds = []
        start = 0
        for i in xrange(num_folds):
            end = start + fold_size
            if i < remainder:
                end += 1
            test = data[start:end]
            train = data[:start] + data[end:]
            folds += [(train, test)]
            start = end
        return folds
    
    def _setupAgent(self, train, agent_class, classification_time_limit, learning_time_limit):
        '''
        Sets up an agent for classification. Includes the learning process.
        
        @param train: The training set - a list of examples and their classification.
        @param agent_class: The agent's class. 
        @param classification_time_limit: The time limit for classification of a single instance.
        @param learning_time_limit: The time limit for learning.
        @return: The agent, ready for classification.
        @raise Exception: If the agent does not return within the time limit.
        '''
        start = time.clock()
        agent = agent_class()
        agent.learn(train[:], classification_time_limit, learning_time_limit)
        cpu_time = time.clock() - start
        if cpu_time > learning_time_limit:
            raise Exception(str(agent) + ' timed out while learning!')
        return agent
    
    def _classify(self, instance, agent, classification_time_limit):
        '''
        Classifies a single instance.
        
        @param instance: The instance to classify - a tuple of features.
        @param agent: The agent classifying agent. 
        @param classification_time_limit: The time limit for classification of a single instance.
        @return: The agent's classification.
        @raise Exception: If the agent does not return within the time limit.
        '''
        start = time.clock()
        classification = agent.classify(instance)
        cpu_time = time.clock() - start
        if cpu_time > classification_time_limit:
            raise Exception(str(agent) + ' timed out while classifying!')
        return classification
    

class ConfusionMatrix:
    '''
    A matrix for aggregating validation results.
    '''
    
    def __init__(self, classes):
        '''
        Initializes an empty matrix.
        
        @param classes: A list of all the possible classification values.
        '''
        self.classes = classes
        self.matrix = {}
        for expected in classes:
            self.matrix[expected] = {}
            for actual in classes:
                self.matrix[expected][actual] = 0
    
    def update(self, expected, actual):
        '''
        Updates the matrix with a new validation result.
        
        @param expected: The expected classification.
        @param actual: The actual classification.
        '''
        self.matrix[expected][actual] += 1
    
    def get(self, expected, actual):
        '''
        @param expected: The expected classification.
        @param actual: The actual classification.
        @return: The number of times the given scenario occurred.
        '''
        return self.matrix[expected][actual]
    
    def getSum(self):
        '''
        @return: The total number of classifications.
        '''
        sum = 0.0
        for expected in self.classes:
            for actual in self.classes:
                sum += self.matrix[expected][actual]
        return sum
    
    def getAccuracy(self):
        '''
        @return: The percentage of correct classifications.
        '''
        correct = 0.0
        for classification in self.classes:
            correct += self.matrix[classification][classification]
        return correct / self.getSum()
    
    def __str__(self):
        '''
        @return: An informative string representation of the matrix.
        '''
        s = '\t'
        for actual in self.classes:
            s += '\tActual'
        s += '\n'
        for actual in self.classes:
            s += '\t' + str(actual)
        s += '\n'
        for expected in self.classes:
            s += 'Expected ' + str(expected)
            for actual in self.classes:
                s += '\t' + str(self.matrix[expected][actual])
            s += '\n'
        s += '\nAccuracy: %.2f%%\n' % (self.getAccuracy()*100)
        return s
    
    def __repr__(self):
        '''
        @return: An informative string representation of the matrix.
        '''
        return str(self)

    
class McNemarMatrix:
    '''
    A matrix for comparing two learning agents.
    '''
    
    def __init__(self, agent1_name, agent2_name):
        '''
        Initializes an empty comparison matrix.
        
        @param agent1_name: The first agent's name.
        @param agent2_name: The second agent's name.
        '''
        self.agent1_name = agent1_name
        self.agent2_name = agent2_name
        self.matrix = {}
        self.matrix[True] = {}
        self.matrix[False] = {}
        self.matrix[True][True] = 0
        self.matrix[True][False] = 0
        self.matrix[False][True] = 0
        self.matrix[False][False] = 0
    
    def update(self, agent1_correct, agent2_correct):
        '''
        Updates the comparison with a new validation result.
        
        @param agent1_correct: Whether the first agent classified correctly.
        @param agent2_correct: Whether the second agent classified correctly.
        '''
        self.matrix[agent1_correct][agent2_correct] += 1
    
    def get(self, agent1_correct, agent2_correct):
        '''
        @param agent1_correct: Whether the first agent classified correctly.
        @param agent2_correct: Whether the second agent classified correctly.
        @return: The number of times the given scenario occurred.
        '''
        return self.matrix[agent1_correct][agent2_correct]
    
    def getSignificance(self):
        '''
        @return: The statistical significance of the comparison. 
                 Higher value means the difference is more significant.
                 Identical agents should return zero.
        '''
        if self.matrix[False][True] < self.matrix[True][False]:
            p = binom_test([self.matrix[True][False], self.matrix[False][True]]) / 2
            return (1.0-p)
        elif self.matrix[False][True] > self.matrix[True][False]:
            p = binom_test([self.matrix[False][True], self.matrix[True][False]]) / 2
            return (1.0-p)
        else:
            return 0.0
    
    def __str__(self):
        '''
        @return: An informative string representation of the comparison.
        '''
        s = '\t\t' + self.agent2_name + '\t' + self.agent2_name + '\n' + \
            '\t\tCorrect\tWrong\n' + \
            self.agent1_name + ' Correct:\t' + str(self.matrix[True][True]) + '\t' + str(self.matrix[True][False]) + '\n' + \
            self.agent1_name + ' Wrong:\t' + str(self.matrix[False][True]) + '\t' + str(self.matrix[False][False]) + '\n' + \
            '\n'
        
        if self.matrix[False][True] < self.matrix[True][False]:
            s += self.agent1_name + ' is better than ' + self.agent2_name + ' with %.2f%% significance.' % (self.getSignificance()*100)
        elif self.matrix[False][True] > self.matrix[True][False]:
            s += self.agent2_name + ' is better than ' + self.agent1_name + ' with %.2f%% significance.' % (self.getSignificance()*100)
        else:
            s += 'Neither agent is better.'
        
        return s
    
    def __repr__(self):
        '''
        @return: An informative string representation of the comparison.
        '''
        return str(self)
    
