# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:24:39 2019

@author: Dorian
"""

from .IRModel import IRModel
import numpy as np


class Vectoriel(IRModel):
    
    def __init__(self, indexerSimple, weighter, normalized):
        super().__init__(indexerSimple)
        self.weighter = weighter
        self.normalized = normalized
        
        
    def getScores(self,query):
        scores = []
        
        index = self.indexerSimple.index     
        
        if self.normalized :
            #Score cosinus
            #prod_scalaire / norm(X)**(1/2) + norm(Y)**(1/2)
            #calcul de norme sqrt(x1**2 + x2**2 + ...
            for doc_i, tf in index.items() :
                q = self.weighter.getWeightsForQuery(query)
                d = self.weighter.getWeightsForDoc(doc_i)
                
                score = 0
                prod_scal = 0
                norm_q = 0
                norm_d = 0
                
                """
                for t,w_q in q.items() :
                    norm_q += w_q**2
                    if t in d :
                        prod_scal += q[t] * d[t]
                for t,w_d in d.items() :
                    norm_d += w_d**2
                """
                
                for i in range(len(q)) :
                    prod_scal += q[i]*d[i]
                    norm_q += q[i]**2
                    norm_d += d[i]**2
                
                score = prod_scal / (np.sqrt(norm_d) + np.sqrt(norm_q))
                
                scores.append((doc_i, score))
                
            
        else : 
            #Produit Scalaire
            for doc_i, tf in index.items() :
                q = self.weighter.getWeightsForQuery(query)
                d = self.weighter.getWeightsForDoc(doc_i)
            
                score = 0
                    
                """
                for t,w_q in q.items() :
                    if t in d :
                        score += w_q * d[t]
                """
                for i in range(len(q)) :
                    score += q[i]*d[i]
                        
                scores.append((doc_i,score))
            
        return scores