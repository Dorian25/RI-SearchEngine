# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:24:33 2019

@author: Dorian
@author: Mouhamad
"""

from .EvalMesure import EvalMesure

class EvalMesureRappel(EvalMesure):
    
    def __init__(self) :
        super().__init__()
    #RAPPEL
    """ 
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
    """   
     
    #RAPPEL AU RANG K (diapo 14) - R@k(q)
    def evalQuery(self,liste, query, k=50) :
        
        #|R|
        nbDocPertinents = len(query.listDocsPertinents)
        if nbDocPertinents == 0 :
            return 0
        kDocs = liste[:min(k,len(liste))]
        
        #jugement de pertinence (document pertinent = 1 //sinon = 0)
        sumJugPertinence = 0
        
        #on parcours les k premiers résultats
        #on regarde s'ils sont pertinents pour la req
        for d in kDocs :
            if d in query.listDocsPertinents :
                sumJugPertinence += 1
                
                
        return (1 / nbDocPertinents) * sumJugPertinence