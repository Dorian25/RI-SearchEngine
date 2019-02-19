# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:11 2019

@author: Dorian
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer
import numpy as np

class Weighter3(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)
        

    def getWeightsForDoc(self,idDoc):
        #weights = self.indexerSimple.index[idDoc] if idDoc in self.indexerSimple.index else {}
        weights = []
        
        for t,v in self.indexerSimple.index_inv.items():
            if idDoc in v :
                weights.append(v[idDoc])
            else:
                weights.append(0)    
        
        return weights
    
 
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem] if stem in self.indexerSimple.index_inv else {}
        return weights
    

    def getWeightsForQuery(self,query):
        """
        porterStemmer = PorterStemmer() 
        weights = porterStemmer.getTextRepresentation(query)
        N = len(self.indexerSimple.index)
        
        for t,v in weights.items():
            #df = nb doc 
            df = len(self.indexerSimple.index_inv[t])
            weights[t] = np.log((N+1)/(1+df))
        
        return weights
        """
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)
        wordsQuery = list(textRepresentation.keys())
        weights = []
        N = len(self.indexerSimple.index)
        
        for t,v in self.indexerSimple.index_inv.items():
            if t in wordsQuery :
                #nb doc contenant t
                df = len(v)
                weights.append(np.log((N+1)/(1+df)))
            else:
                weights.append(0)
    
        return weights