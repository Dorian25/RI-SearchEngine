# -*- coding: utf-8 -*-
"""
Created on Sat Feb 16 17:02:25 2019

@author: Dorian
"""

from abc import ABC, abstractmethod

class Weighter(ABC):
    
    def __init__(self, indexerSimple) :
        self.indexerSimple = indexerSimple
        super().__init__()
        
    @abstractmethod
    def getWeightsForDoc(idDoc):
        """
        La methode abstraitegetWeightsForDoc(idDoc) qui retourne
        les poids des termes pour un documentdont l’identifiant est idDoc.
        """
        pass
    
    @abstractmethod
    def getWeightsForStem(stem):
        """
        La methode abstraite getWeightsForStem(stem) qui retourne les 
        poids du terme stem pour tous les documents qui le contiennent.
        """
        pass
    
    @abstractmethod
    def getWeightsForQuery(query):
        """
        La methode abstraite getWeightsForQuery(query) qui retourne
        les poids des termes de la requete.
        """
        pass