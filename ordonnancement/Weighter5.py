# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:05:01 2019

@author: Dorian
"""

from .Weighter import Weighter
from indexation.TextRepresenter import PorterStemmer
import numpy as np

class Weighter5(Weighter):
    
    def __init__(self, indexerSimple) :
        super().__init__(indexerSimple)
        
    """    
       d1 | d2 | d3 
    t1  1    0    4
    t2  1    1    3
    t3  0    3    1
    t4  1    0    0 
    ...
    tn  0    1    0
    """    
    #taille vecteur = nb mots de la collection
    def getWeightsForDoc(self,idDoc):
        weights = []
        #nb doc de la collection
        N = len(self.indexerSimple.index)
        
        for t,v in self.indexerSimple.index_inv.items():
            if idDoc in v :
                #nb doc contenant t
                df = len(v)
                idf = np.log((N+1)/(1+df))
                weights.append((1+np.log(v[idDoc]))*idf)
            else:
                weights.append(0)    
        
        return weights
    
 
    def getWeightsForStem(self,stem):
        pass
    

    def getWeightsForQuery(self,query):
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)
        wordsQuery = list(textRepresentation.keys())
        weights = []
        N = len(self.indexerSimple.index)
        
        for t,v in self.indexerSimple.index_inv.items():
            if t in wordsQuery :
                #nb doc contenant t
                df = len(v)
                idf = np.log((N+1)/(1+df))
                weights.append((1+np.log(textRepresentation[t]))*idf)
            else:
                weights.append(0)
    
        return weights