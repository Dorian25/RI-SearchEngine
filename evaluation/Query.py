#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:45:45 2019

@author: Dorian
@author: Mouhamad
"""


#Classe représentant une requête
class Query:
    def __init__(self):
        """Constructeur pour la classe."""
        self._I = ""
        self._A = ""
        self._N = ""
        self._W = ""
        self._listDocsPertinents = []
        
    def _get_I(self):
        return self._I
    def _set_I(self, new_I):
        self._I = new_I
        
    def _get_A(self):
        return self._A
    def _set_A(self, new_A):
        self._A = new_A
        
    def _get_N(self):
        return self._N
    def _set_N(self, new_N):
        self._N = new_N
        
    def _get_W(self):
        return self._W
    def _set_W(self, new_W):
        self._W = new_W
        
    def _get_listDocsPertinents(self):
        return self._listDocsPertinents
    def _set_listDocsPertinents(self,new_list):
        self._listDocsPertinents = new_list
        
    I = property(_get_I,_set_I)
    A = property(_get_A, _set_A)
    W = property(_get_W, _set_W)
    N = property(_get_N, _set_N)
    listDocsPertinents = property(_get_listDocsPertinents,_set_listDocsPertinents)