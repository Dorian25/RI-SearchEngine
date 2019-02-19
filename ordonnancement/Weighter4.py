# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:00 2019

@author: Dorian
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer
import numpy as np

class Weighter4(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)
        

    def getWeightsForDoc(self,idDoc):
        """
        weights = self.indexerSimple.index[idDoc] if idDoc in self.indexerSimple.index else {}
        for t,v in weights.items():
            weights[t] = 1+np.log(weights[t])
        
        
        return weights
        """
    
        weights = []
        
        for t,v in self.indexerSimple.index_inv.items():
            if idDoc in v :
                weights.append(1+np.log(v[idDoc]))
            else:
                weights.append(0)    
        
        return weights
    
 
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem] if stem in self.indexerSimple.index_inv else {}
        if weights :
            for doc_i,v in weights.items():
                weights[doc_i] = 1+np.log(weights[doc_i])
        
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