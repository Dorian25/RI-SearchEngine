# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:21:35 2019

@author: Dorian
@author: Mouhamad
"""

from .EvalMesure import EvalMesure

class EvalMesurePrecision(EvalMesure):
    
    def __init__(self) :
        super().__init__()
    
    #tp/(tp+fp)
    def evalQuery(liste, query):
        #tp
        nbDocPertSelect = 0
        #fp
        nbDocNotPertSelect = 0
        
        docsPert = query.listDocsPertinents
        
        for docI in liste :
            if docI in docsPert :
                nbDocPertSelect += 1
            else :
                nbDocNotPertSelect += 1
                
        return nbDocPertSelect / (nbDocPertSelect + nbDocNotPertSelect)

        
        