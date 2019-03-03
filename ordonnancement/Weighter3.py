# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:11 2019

@author: Dorian
@author: Mouhamad
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer
import numpy as np

class Weighter3(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)    

    def getWeightsForDoc(self,idDoc):
        weights = self.indexerSimple.index[idDoc].copy() if idDoc in self.indexerSimple.index else {}
        return weights 
 
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem].copy() if stem in self.indexerSimple.index_inv else {}
        return weights
        
    def getWeightsForQuery(self,query):
        porterStemmer = PorterStemmer() 
        weights = porterStemmer.getTextRepresentation(query)
        N = len(self.indexerSimple.index)
        
        for t,v in weights.items():
            #df = nb doc contenant t
            df = len(self.indexerSimple.index_inv[t]) if t in self.indexerSimple.index_inv else 0
            weights[t] = np.log((N+1)/(1+df))
        
        return weights