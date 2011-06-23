class Classifier:
    '''
    A generic classifier interface.
    '''
    
    def classify(self, instance):
        '''
        Classifies the given instance.
        
        @param instance: A tuple of features.
        @return: The instance's classification, according to this classifier.
        '''
        raise NotImplementedError()
    
    def learn(self, examples, classification_time_limit, learning_time_limit):
        '''
        Learns the classifier from the given examples.
        
        @param examples: A list of (instance, classification) tuples.
                         The instances are equal-lengthed tuples of features.
        @param classification_time_limit: The time limit for classification of a single instance.
        @param learning_time_limit: The time limit for learning.
        '''
        raise NotImplementedError()