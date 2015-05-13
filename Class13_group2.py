import numpy as np
class Data:
    
    def __init__(self, fileName):
        self.filename = filename
        self.data = np.empty([0,2])
        self.varNames = []
        
    def getVarNames(self):
        return self.varNames
    
    def GetData(self):
        return self.data
        
    def GetCol(self,ColNum):
        
        return self.data[:,ColNum]
        
