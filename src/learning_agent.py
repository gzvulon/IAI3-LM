import time

class LearningAgent:
    '''
    This is the interface and abstract implementation of a learning agent.
    '''
    
    def classify(self, raw_instance):
        '''
        Classifies a raw instance.
        
        @param raw_instance: A raw instance.
        @return: The given instance's predicted classification.
        '''
        instance = self.extractor.extract(raw_instance)
        return self.classifier.classify(instance)
    
    def learn(self, examples, classification_time_limit, learning_time_limit):
        '''
        Sets up the feature extractor and learns the classifier from the given examples.
        
        @param examples: A list of (data, classification) tuples.
        @param classification_time_limit: The time limit for classification of a single instance.
        @param learning_time_limit: The time limit for learning.
        '''
        start = time.clock()
        
        raw_data = [example[0] for example in examples]
        self.extractor = self.createFeatureExtractor()
        self.extractor.setup(raw_data, classification_time_limit, learning_time_limit)
        
        processed_examples = []
        for raw_example, classification in examples:
            processed_examples += [(self.extractor.extract(raw_example), classification)]
        
        cpu_time = time.clock() - start
        time_left = learning_time_limit - cpu_time
        
        self.classifier = self.createClassifier()
        self.classifier.learn(processed_examples, classification_time_limit, time_left)
    
    def createFeatureExtractor(self):
        '''
        @return: An uninitialized feature extractor instance.
        '''
        raise NotImplementedError()
    
    def createClassifier(self):
        '''
        @return: An uninitialized classifier instance.
        '''
        raise NotImplementedError()
    
    def __str__(self):
        '''
        @return: The agent's name.
        '''
        raise NotImplementedError()
    
    def __repr__(self):
        '''
        @return: The agent's name.
        '''
        return str(self)
    
