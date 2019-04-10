# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:33:54 2019

@author: Dorian
"""

class PageRank:
    
    def __init__(self, index):
        self.index = index
    
    def getSubGraph(self, candidates, n, k) :
        """ determiner le sous graphe G_Q = (V_Q,E_Q)"""
        
        #n = nb doc seeds à considerer
        #k = nb lien entrant à considerer pour chaque doc seed
        
        seeds = candidates[0:n]
        V_Q = []
        S = []
        
        #Initialisation de V_Q
        
        

        #Pour chaque doc D dans S
        #ajout dans V_Q de tous les docs pointés par D et 
        #de k documents choisis random parmis ceux pointant vers D
        
        for d in seeds :
            doc_pointed = self.index.getHyperlinksFrom(d)
            V_Q =  
            
        
        
        
        return V_Q
        
        
    def pageRank(candidates, n, k, epsilon, max_iter=100) : 3
        V_Q,E_Q = self.getSubGraph(candidates,n,k)