import numpy as np
class Normalize(object):  
    maxAttr=0
    minAttr=0
    def __init__(self,x):
        self.x = np.asmatrix(x)
        self.maxAttr=np.zeros(self.x.shape[1])
        self.minAttr=np.zeros(self.x.shape[1])
    def fit(self): ## must take min value and max value. I'll use numpy to take this
        ## normalize = (value-min)/(max-min)
        x_return = self.x.transpose()
        for (i,col) in zip((range(0,self.x.shape[1])),(x_return)):
            self.maxAttr[i]=col.max()
            self.minAttr[i]=col.min()
        return self.x
    def transform(self): 
        aux = np.asmatrix(np.zeros((self.x.shape[1],self.x.shape[0]))) 
        self.x = self.x.transpose()            
        for (index,coluna) in zip((range(0,aux.shape[0])),(self.x)):
            aux[index]= ((coluna - self.minAttr[index])/( self.maxAttr[index] - self.minAttr[index]))
        self.x = aux
        self.x = self.x.transpose()                      
        return self.x    
class Standardize(object):
    mean=0
    std=0
    def __init__(self,x):
        self.x = np.asmatrix(x)        
        self.mean = np.zeros(self.x.shape[1])
        self.std  = np.zeros(self.x.shape[1])        
    def fit(self):
        x_return = self.x.transpose()
        for (i,col) in zip((range(0,self.x.shape[1])),(x_return)):            
            self.mean[i]=col.mean()
            self.std[i]=col.std()
        return self.x
    def transform(self): 
        aux = np.asmatrix(np.zeros((self.x.shape[1],self.x.shape[0]))) 
        self.x = self.x.transpose()            
        for (index,coluna) in zip((range(0,aux.shape[0])),(self.x)):
            aux[index]= ((coluna - self.mean[index])/( self.std[index]))
        self.x = aux
        self.x = self.x.transpose()   
        return self.x