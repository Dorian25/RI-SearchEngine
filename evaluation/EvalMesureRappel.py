# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:24:33 2019

@author: Dorian
"""

from .EvalMesure import EvalMesure

class EvalMesureRappel(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    #tp / (tp + fn)
    def evalQuery(liste, query):
        #tp
        nbDocPertSelect = 0
        #fn
        nbDocPertNotSelect = 0
        
        docsPert = query.listDocsPertinents
        
        for docI in liste :
            if docI in docsPert:
                nbDocPertSelect += 1
            
            
        for docI in docsPert :
            if docI not in liste :
                nbDocPertNotSelect += 1
                
        return nbDocPertSelect / (nbDocPertNotSelect + nbDocPertSelect)
        
        