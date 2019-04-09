# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:24:39 2019

@author: Dorian
@author: Mouhamad
"""

from .IRModel import IRModel
import numpy as np
from indexation.TextRepresenter import PorterStemmer

class Vectoriel(IRModel):
    
    def __init__(self, indexerSimple, weighter, normalized):
        super().__init__(indexerSimple)
        self.weighter = weighter
        self.normalized = normalized
    
    def getScores(self,query):
        scores = {}
        
        index_inv = self.indexerSimple.index_inv
        
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)
        terms_q = list(textRepresentation.keys())
        
        q = self.weighter.getWeightsForQuery(query)
    
        norme_q = np.sqrt(sum([v**2 for v in q.values()]))
        #k=idDoc ; v=normeDoc
        normes_docs = {}
    
        if self.normalized :
            #Score cosinus
            #prod_scalaire / norm(X)**(1/2) + norm(Y)**(1/2)
            #calcul de norme sqrt(x1**2 + x2**2 + ...
            for tq,poids_tq in q.items() :
                #on ne garde que les docs qui contiennent le terme tq de la query
                if tq in index_inv :
                    for doc_i in index_inv[tq].keys():
                        d = self.weighter.getWeightsForDoc(doc_i)
                        #on calcule la norme du doc_i et on l'ajoute dans le dico
                        #s'il n'est pas présent
                    
                        if doc_i not in normes_docs.items():
                            normes_docs[doc_i] = np.sqrt(sum([v**2 for v in d.values()]))
                            
                        score = poids_tq * d[tq]
                        
                        if doc_i in scores:
                            scores[doc_i] += score
                        else :
                            scores[doc_i] = score
                        
            #prod_scalaire / norm(X)**(1/2) + norm(Y)**(1/2)  
            for doc_i in scores.keys():
                 scores[doc_i] /= (norme_q + normes_docs[doc_i])
                
        else : 
            #Produit Scalaire
            for t in terms_q:
                if t in index_inv :
                    for doc_i in index_inv[t].keys():
                        d = self.weighter.getWeightsForDoc(doc_i)
                    
                        score = q[t] * d[t]
                        
                        if doc_i in scores:
                            scores[doc_i] += score
                        else :
                            scores[doc_i] = score
            
        return scores