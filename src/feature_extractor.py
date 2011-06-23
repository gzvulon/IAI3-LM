class FeatureExtractor:
    '''
    Extracts features from raw data.
    '''
    
    def extract(self, raw_instance):
        '''
        Creates a new instance in the feature-space from the given raw instance.
        
        @param raw_instance: A raw instance.
        @return: A tuple of features.
        '''
        raise NotImplementedError
    
    def setup(self, examples, extraction_time_limit, setup_time_limit):
        '''
        Prepares the feature extractor.
        
        @param examples: A list of raw data examples.
        @param extraction_time_limit: The time limit for extraction of a 
                                      single example.
        @param setup_time_limit: The time limit for setting up the extractor.
        '''
        raise NotImplementedError
    
