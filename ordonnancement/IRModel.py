# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:01:07 2019

@author: Dorian
"""

from abc import ABC, abstractmethod

class IRModel(ABC):
    
    def __init__(self, indexerSimple) :
        self.indexerSimple = indexerSimple
        super().__init__()
        
    @abstractmethod
    def getScores(query):
        pass
    
    def getRanking(self,query):
        return sorted(self.getScores(query), key = lambda score : score[1], reverse = True)