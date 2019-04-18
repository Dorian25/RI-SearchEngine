# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:55:57 2019

@author: Dorian
@author: Mouhamad
"""

from .EvalMesure import EvalMesure

#source = https://en.wikipedia.org/wiki/Mean_reciprocal_rank
class EvalMesureReciprocalRank(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(self,liste, query):
        
        #refers to the rank position of the first relevant document for the query
        for i in range(len(liste)) :
            if liste[i] in query.listDocsPertinents :
                return 1/i
        #If none of the proposed results are correct, reciprocal rank is 0.    
        return 0