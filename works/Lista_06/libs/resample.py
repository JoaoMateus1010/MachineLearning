import numpy as np
class Functions(object):
    def __init__(self,x):        
        self.x = np.asarray(x)        
    def split_stratified_train_test(self,y,perc_train=0.7, seed=1):        
        #implementação da funcionalidade random
        np.random.seed(seed)                
        index = range(0,y.size)
        index = np.asarray(index)
        np.random.shuffle(index)        
        #implementação da funcionalidade de divisão entre train e test
        lines_dataSet = y.size
        porcent = 100*perc_train
        indexDivision = round(((porcent*lines_dataSet)/100))
        #criar array com index dos dados de treino e teste   
        arrayTrain = index[:indexDivision]
        arrayTeste = index[indexDivision:,]
        return (arrayTrain,arrayTeste)