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