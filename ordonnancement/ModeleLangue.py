# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:36:13 2019

@author: Dorian
@author: Mouhamad
"""

from .IRModel import IRModel
from indexation.TextRepresenter import PorterStemmer

class ModeleLangue(IRModel):
    
    def __init__(self,indexerSimple):
        super().__init__(indexerSimple)
        
    def getScores(self, query):
        scores = {}
        
        index_inv = self.indexerSimple.index_inv
        index = self.indexerSimple.index
        
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)
        terms_q = list(textRepresentation.keys())
        
        #somme des fréquences de tous les termes de la collection
        total_tf_c = 0
        for t,tf in index_inv.items():
            total_tf_c += sum(tf.values())    
    
        #si la requete est courte alors lambda = 0.8 sinon 0.2
        lbda = 0.8 if len(query.split()) <= 3 else 0.2
        
        for t in terms_q:
            if t in index_inv :
                for doc_i,tf in index_inv[t].items():
                    total_tf_d = sum(index[doc_i].values())
                        
                    tf_w = index[doc_i][t] if t in index[doc_i] else 0
                    #fréquence du terme dans la collection
                    total_tf_t = sum(index_inv[t].values()) if t in index_inv else 0
                        
                    pT_Md = 0 if tf_w == 0 or total_tf_d == 0 else tf_w / total_tf_d
                    pT_Mc = 0 if total_tf_t == 0 or total_tf_c == 0 else total_tf_t / total_tf_c
              
                    score = (1-lbda) * (pT_Md) + lbda * (pT_Mc)
                        
                    if doc_i in scores:
                        scores[doc_i] *= score
                    else:
                        scores[doc_i] = score
            
        return scores