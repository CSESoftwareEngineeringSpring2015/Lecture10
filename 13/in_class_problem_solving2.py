import numpy as np

# I changed some stuff, but kept it similar to what you all wrote for the code.
# This was to make sure that the code at least runs correctly. Added some
# extra comments.
class Data(object):
    
    def __init__(self, filename):
        self.filename = filename
        self.headers = [] # Better to be specific than using None
        self.data = [[], []] # Better to be specific than using None
        
    def read(self):
        got_header = False
        for line in open(self.filename, 'r'):
            fields = line.strip().split(",")
            if not got_header:
                self.headers.append(fields[0])
                self.headers.append(fields[1])
                got_header = True
            else:
                self.data[0].append(float(fields[0]))
                self.data[1].append(float(fields[1]))
        self.data = np.array(self.data)
        
    def getVarNames(self):
        return self.headers
    
    def getData(self):
        return self.data
    
    def getCol(self, colNum):
        return None # Placeholder code: delete!
        # Why does this not work? Hint: numpy
        # return self.data[:, colNum]
        
class EnzymeData(Data):
    
    def __init__(self):
        super(EnzymeData, self).__init__("09_THDPA.csv")
    
    # Wanted parameterMichaelis method
    def returnVMax():
        return None # Placeholder code: delete!
        # Why does this code not work? How do you get both Vmax and Km?
        '''data = filename.getData()
        np.matrix(data)
        invert = 1./data
        lenCol = len(filename.getCol())
        np.ones(1, lenCol)'''
  
# How do you see the output in the console?      
michaelisObj = EnzymeData()
michaelisObj.getVarNames()
# This line does not work, why?
# michaelisObj.getCol()
michaelisObj.getData()

# How do you read the csv file and use other methods?
# What can you do to make this code better? To plot?