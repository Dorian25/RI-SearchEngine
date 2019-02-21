# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:36:13 2019

@author: Dorian
@author: Abdela

source 1 : https://fr.wikipedia.org/wiki/Okapi_BM25
"""

from .IRModel import IRModel 
import numpy as np
from indexation.TextRepresenter import PorterStemmer

#Okapi-BM25 - diapo 21 (Cours 2 - Modèles d'appariement)
class Okapi(IRModel):
    
    def __init___(self,indexerSimple):
        super().__init__(indexerSimple)
        
    def getScores(self,query):
        scores = []
        
        index = self.indexerSimple.index
        index_inv = self.indexerSimple.index_inv
        
        #On calcul la longueur moyenne des documents dans la collection considérée
        # ?? 
        # longueur doc = nb terme distinct ou somme des tf d'un doc
        sumLength = 0
        for k,v in index.items():
            #nb mots distincts
            #sumLength += len(v)
            sumLength += sum(v.values())
        N = len(index)
        avgdl = sumLength / N

        b = 0.75
        k1 = 1.2
        
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)
        wordsQuery = list(textRepresentation.keys())
        
        for doc_i,tf in index.items() :
            score = 0
            longDoc = sum(tf.values())
            
            for qi in wordsQuery :
                #nb documents contenant qi
                n_qi = len(index_inv[qi]) if qi in index_inv else 0
                
                IDF_qi = np.log((N - n_qi + 0.5) / (n_qi + 0.5))
                
                # frequence d'un terme == tf ==  nombre d'occurrences de ce terme
                f_qi_D = tf[qi] if qi in tf else 0
                
                score += IDF_qi * (f_qi_D * (k1 + 1)) / (f_qi_D + k1 * (1 - b + b * longDoc/avgdl))               
            
            
            scores.append((doc_i,score))
        
        return scores
    
        