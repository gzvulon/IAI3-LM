import time
from random import Random

class AgentAnalyzer:
    '''
    Compares two learning agents by cross-validation and 
    McNemar's test for statistical significance.
    '''
    def run_one(self, data, agent1_class, classification_time_limit, learning_time_limit, num_folds = 2, seed = 1):
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
        
        shuffled_data = data[:]
        rnd = Random(seed)
        rnd.shuffle(shuffled_data)
        
        for train, test in self._createFolds(shuffled_data, num_folds):
            agent1 = self._setupAgent(train, agent1_class, classification_time_limit, learning_time_limit)
            
            for test_instance, test_classification in test:
                classification1 = self._classify(test_instance, agent1, classification_time_limit)
                
                confusion1.update(test_classification, classification1)
        
        return confusion1
    
        
    
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

