# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:55:27 2019

@author: Dorian
"""

from .EvalMesure import EvalMesure

class EvalMesureNDCG(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(liste, query):