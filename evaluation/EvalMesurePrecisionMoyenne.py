# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 17:50:19 2019

@author: Dorian
@author: Mouhamad
"""

from .EvalMesure import EvalMesure
from .EvalMesurePrecision import EvalMesurePrecision

#diapo 20 AvgP
class EvalMesurePrecisionMoyenne(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(self,liste, query, k=3):
        
        #(n_+)^q
        nbDocPertinents = len(query.listDocsPertinents)
        
        sumJugPrecision = 0
    
        for i in range(len(liste)) :
            
            if liste[i] in query.listDocsPertinents :
                
                sumJugPrecision += EvalMesurePrecision().evalQuery(liste,query,i)
            
        return (1 / nbDocPertinents) * sumJugPrecision