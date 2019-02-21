# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 18:36:13 2019

@author: Dorian
@author: Abdela
"""

from .IRModel import IRModel
from indexation.TextRepresenter import PorterStemmer

class ModeleLangue(IRModel):
    
    def __init__(self,indexerSimple):
        super().__init__(indexerSimple)
        
    def getScores(self, query):
        scores = []
        
        index = self.indexerSimple.index
        index_inv = self.indexerSimple.index_inv
        
        porterStemmer = PorterStemmer() 
        textRepresentation = porterStemmer.getTextRepresentation(query)        
        wordsQuery = list(textRepresentation.keys())
        
        #somme des fréquences de tous les termes de la collection
        total_tf_c = 0
        for t,tf in index_inv.items():
            total_tf_c += sum(tf.values())
            
     
        #si la requete est longue alors lambda = 0.8
        if len(query.split()) <= 3 :
            lbda = 0.8
            
            for doc_i,tf in index.items():
                score = 1
                total_tf_d = sum(tf.values())
                
                for w in wordsQuery:
                    tf_w = tf[w] if w in tf else 0
                    #fréquence du terme dans la collection
                    total_tf_t = sum(index_inv[w].values()) if w in index_inv else 0
                    
                    pT_Md = 0 if tf_w == 0 or total_tf_d == 0 else tf_w / total_tf_d
                    pT_Mc = 0 if total_tf_t == 0 or total_tf_c == 0 else total_tf_t / total_tf_c
          
                    score *= (1-lbda) * (pT_Md) + lbda * (pT_Mc)
        
                scores.append((doc_i,score))
        #sinon lambda = 0.2
        else : 
            lbda = 0.2
            
            for doc_i,tf in index.items():
                score = 1
                total_tf_d = sum(tf.values())
                
                for w in wordsQuery:
                    tf_w = tf[w] if w in tf else 0
                    #fréquence du terme dans la collection
                    total_tf_t = sum(index_inv[w].values()) if w in index_inv else 0
                    
                    pT_Md = 0 if tf_w == 0 or total_tf_d == 0 else tf_w / total_tf_d
                    pT_Mc = 0 if total_tf_t == 0 or total_tf_c == 0 else total_tf_t / total_tf_c
                    
                    score *= (1-lbda) * (pT_Md) + lbda * (pT_Mc)
                
                scores.append((doc_i,score))
            
        return scores