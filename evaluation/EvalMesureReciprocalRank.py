# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:55:57 2019

@author: Dorian
"""

.from EvalMesure import EvalMesure

class EvalMesureReciprocalRank(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(liste, query):
        
        docsPert = query.listDocsPertinents
        
        for i in range(len(liste)) :
            if doc[i] in docsPert :
                return 1/i
            
        return -1