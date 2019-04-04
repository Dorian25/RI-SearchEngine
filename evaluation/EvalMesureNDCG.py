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
        
    def evalQuery(self,liste, query, p=3):        
        
        #pertinence graduée du document 1
        rel1 = 1 if liste[0] in query.listDocsPertinents else 0
        
        sum_in_DCG = 0
        sum_in_IDCG = 0
        #on prend p docs sans prendre le premier
        for i in range(1,p) :
            if liste[i] in query.listDocsPertinents :
                sum_in_DCG += 1 / log2(i+1)
        #les documents apparaissant à un rang élevé seront penalisés par le log2
        DCG = rel1 + sum_in_DCG
        
        #nb doc pertinent <= p
        for i in range(p) :
            sum_in_IDCG +=  ((2**1)-1) / log2(i+2)
        
        #ideal DCG = maximum possible DCG through position p
        IDCG = sum_in_IDCG
        
        return DCG / IDCG