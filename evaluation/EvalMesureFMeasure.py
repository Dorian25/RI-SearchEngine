# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:25:05 2019

@author: Dorian
"""

from .EvalMesure import EvalMesure
from .EvalMesurePrecision import EvalMesurePrecision
from .EvalMesureRappel import EvalMesureRappel

class EvalMesureFMeasure(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(liste, query):
        precision = EvalMesurePrecision().evalQuery(liste, query)
        rappel = EvalMesureRappel().evalQuery(liste, query)
        
        return 2 * (precision * rappel) / (precision + rappel)