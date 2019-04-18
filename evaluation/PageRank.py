# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 14:33:54 2019

@author: Dorian
@author: Mouhamad
"""

import numpy as np

class PageRank:
    
    def __init__(self, index):
        self.index = index
    
    def getSubGraph(self, candidates, n, k) :
        """ determiner le sous graphe G_Q = (V_Q,E_Q)"""
        
        #n = nb doc seeds à considerer
        #k = nb lien entrant à considerer pour chaque doc seed
        
        seeds = candidates[:min(n,len(candidates))]
        V_Q = {}        

        #Pour chaque doc D dans S
        #ajout dans V_Q de tous les docs pointés par D et 
        #de k documents choisis random parmis ceux pointant vers D
        
        for d in seeds :
            doc_to = list(self.index.getHyperlinksTo(d).keys())
            doc_from = self.index.getHyperlinksFrom(d)
            doc_from_id = list(doc_from.keys())
            if k < len(doc_from):
                doc_from_cm = np.array([doc_from[i] for i in doc_from_id]).cumsum()
                tampon = []
                for i in range(k):
                    ind = np.searchsorted(doc_from_cm, np.random.rand()*doc_from_cm[-1])
                    tampon.append(doc_from_id[ind])
                doc_from_id = tampon
            V_Q[d] = doc_to + doc_from_id
            
        return V_Q
        
        
    def pageRank(self,candidates, n, k, max_iter=100, d = 0.85, a = 1, e = 0.001) :
        
        G = self.getSubGraph(candidates,n,k)
        
        nodes = set()
        
        for noeud, noeuds in G.items():
            nodes |= set(noeud) | set(noeuds)
            
        nodes = list(nodes)
        
        n = len(nodes)
        
        A = {}
        for i in nodes:
            if i in G:
                for j in G[i]:
                    if (i,j) in A.keys():
                        A[i,j] += 1
                    else:
                        A[i,j] = 1

                    
        D = {node : 0 for node in nodes }
        for v in G.values():
            for i in v:
                D[i] += 1
        
        P = {}
        for i,j in A.keys():
            P[i,j] = A[i,j] / D[j]
        ite = 0
        
        St = {node : 0 for node in nodes}
        Stplus1 = {node : 1/n for node in nodes}
        diff = 1
        
        #a revoir condition de la boucle
        #pour juste s'occuper de la convergence
        while diff >= e and max_iter > ite:
            St = Stplus1.copy()
            for i in nodes:
                if i in G:
                    Stplus1[i] = d * sum([P[i,j] * St[j] for j in G[i]]) + (1-d)*a
            somme = sum(Stplus1.values())
            for i in nodes:
                Stplus1[i] /= somme
            diff = sum([np.abs(Stplus1[node] - St[node]) for node in nodes])
            ite += 1
            
        
        return sorted(Stplus1.items(), key = lambda score : score[1], reverse = True)