# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 16:15:54 2019

@author: Dorian
@author: Mouhamad
"""

from abc import ABC, abstractmethod

class EvalMesure(ABC):
    
    def __init__(self) :
        super().__init__()
        
    @abstractmethod
    def evalQuery(liste, query):
        """
        permettant de calculer la mesure pour la liste des documents retournes 
        par un modele et un objet Query.
        """
        pass