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
    
    #PRECISION
    """
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
    """

    #PRECISION AU RANG K (diapo 14) - P@k(q)
    def evalQuery(self, liste, query, k=2) :
        
        kDocs = liste[:k]
        
        #jugement de pertinence (document pertinent = 1 //sinon = 0)
        sumJugPertinence = 0
        
        #on parcours les k premiers résultats
        #on regarde s'ils sont pertinents pour la req
        for d in kDocs :
            if d in query.listDocsPertinents :
                sumJugPertinence += 1
                
                
        return (1 / k) * sumJugPertinence        