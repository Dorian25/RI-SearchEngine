# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:00 2019

@author: Dorian
@author: Abdela
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer

class Weighter2(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)
        
    def getWeightsForDoc(self,idDoc):
        weights = self.indexerSimple.index[idDoc] if idDoc in self.indexerSimple.index else {}
        return weights  
 
    def getWeightsForStem(self,stem):
        weights = self.indexerSimple.index_inv[stem] if stem in self.indexerSimple.index_inv else {}
        return weights
    
    def getWeightsForQuery(self,query):
        porterStemmer = PorterStemmer() 
        weights = porterStemmer.getTextRepresentation(query)
        return weights