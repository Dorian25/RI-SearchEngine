# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:55:27 2019

@author: Dorian
@author: Mouhamad
"""
#source = https://opensourceconnections.com/blog/2018/02/26/ndcg-scorer-in-quepid/
#source = https://en.wikipedia.org/wiki/Discounted_cumulative_gain
from .EvalMesure import EvalMesure
from math import log2

#diapo 23/24
class EvalMesureNDCG(EvalMesure):
    
    def __init__(self) :
        super().__init__()
        
    def evalQuery(self,liste, query, p=50):  
        p = min(p, len(liste))
        if not liste :
            return 0
                
        DCG = 0
        IDCG = 0
        #on prend p docs sans prendre le premier
        for i in range(p) :
            if liste[i] in query.listDocsPertinents :
                DCG += 1 / log2(i+2)
        #les documents apparaissant à un rang élevé seront penalisés par le log2
        
        #nb doc pertinent <= p
        for i in range(len(liste)) :
            reli = liste[i] in query.listDocsPertinents
            IDCG +=  (2**reli - 1) / log2(i+2)
        
        #ideal DCG = maximum possible DCG through position p
        if IDCG == 0:
            return 0
        
        return DCG / IDCG