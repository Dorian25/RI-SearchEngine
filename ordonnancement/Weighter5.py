# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:01 2019

@author: Dorian
@author: Abdela
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer
import numpy as np

class Weighter5(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)   
    
    def getWeightsForDoc(self,idDoc):
        weights = self.indexerSimple.index[idDoc] if idDoc in self.indexerSimple.index else {}
        #nb doc de la collection
        N = len(self.indexerSimple.index)
        
        for t,v in weights.items():
            #nb doc contenant t
            df = len(self.indexerSimple.index_inv[t])
            idf = np.log((N+1)/(1+df))
            weights[t]  = (1+np.log(v))*idf
            
        return weights
        
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem] if stem in self.indexerSimple.index_inv else {}
        #nb doc de la collection
        N = len(self.indexerSimple.index)
        
        for doc_i,v in weights.items():
            #nb doc contenant t
            df = len(weights)
            idf = np.log((N+1)/(1+df))
            weights[doc_i] = (1+np.log(v))*idf
        
        return weights
    
    
    def getWeightsForQuery(self,query):
        porterStemmer = PorterStemmer() 
        weights = porterStemmer.getTextRepresentation(query)
        N = len(self.indexerSimple.index)
        
        for t,v in weights.items():
            #df = nb doc contenant t
            df = len(self.indexerSimple.index_inv[t]) if t in self.indexerSimple.index_inv else 0
            idf = np.log((N+1)/(1+df))
            weights[t]  = (1+np.log(v))*idf
        
        return weights