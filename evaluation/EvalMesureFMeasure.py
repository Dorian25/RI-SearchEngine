# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:25:05 2019

@author: Dorian
"""

from .EvalMesure import EvalMesure
from .EvalMesurePrecision import EvalMesurePrecision
from .EvalMesureRappel import EvalMesureRappel

#diapo 13
class EvalMesureFMeasure(EvalMesure):
    
    def __init__(self) :
        super().__init__()
     
    #F MEASURE
    """
    def evalQuery(liste, query):
        precision = EvalMesurePrecision().evalQuery(liste, query)
        rappel = EvalMesureRappel().evalQuery(liste, query)
        
        return 2 * (precision * rappel) / (precision + rappel)
    """
    
    #F MEASURE AU RANG K
    def evalQuery(self,liste, query, k=2, beta=1):
        
        precision = EvalMesurePrecision().evalQuery(liste, query, k)
        if precision == 0 :
            return 0
        rappel = EvalMesureRappel().evalQuery(liste, query, k)
        if rappel == 0 :
            return 0
        return (1+beta**2) * (precision * rappel) / (((beta**2) *precision) + rappel)