from classifier import Classifier

# A bloody large number.
INFINITY = 1.0e400

class NearestNeighbor(Classifier):
    '''
    A very basic implementation of the nearest-neighbor learning algorithm.
    '''
    
    def classify(self, instance):
        '''
        Finds the closest example to the given instance (in terms of Euclidean distance), 
        and returns its class.
        
        @param instance: A tuple of numerical features.
        @return: The nearest neighbor's class.
        '''
        min_distance = INFINITY
        min_classification = None
        for example, classification in self.examples:
            d = self._distance(instance, example)
            if d < min_distance:
                min_distance = d
                min_classification = classification
        return min_classification
    
    def learn(self, examples, classification_time_limit, learning_time_limit):
        '''
        Learns the classifier from the given examples.
        
        @param examples: A list of (instance, classification) tuples.
                         The instances are equal-lengthed tuples of features.
        @param classification_time_limit: The time limit for classification of a single instance.
        @param learning_time_limit: The time limit for learning.
        '''
        self.examples = examples
    
    def _distance(self, x, y):
        if len(x) != len(y):
            raise IndexError
        return sum((x[i] - y[i])**2 for i in xrange(len(x)))
