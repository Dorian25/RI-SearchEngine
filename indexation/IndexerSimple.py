# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:23:55 2019

@author: Dorian

source_1 : https://stackoverflow.com/questions/21453117/json-dumps-not-working
"""
#index norm et index inv norm a faire
import json
import math
from .TextRepresenter import PorterStemmer

class IndexerSimple:
    
    def __init__(self,name_collection):
        self.name_collection = name_collection
        self._index = {}
        self._index_inv = {}
        self._index_norm = {}
        self._index_inv_norm = {}
        
    def indexation(self,documents):
        
        for i,doc in documents.items() :
            
            porterStemmer = PorterStemmer() 
            textRepresentation = porterStemmer.getTextRepresentation(doc.T)
            self.index[doc.I] = textRepresentation
            
            for k,v in textRepresentation.items() :
                if k in self.index_inv :
                    self.index_inv[k].update({doc.I : self.index[doc.I][k]})
                else :
                    self.index_inv[k] = {}
                    self.index_inv[k].update({doc.I : self.index[doc.I][k]})
                    
        name_f_index = "index_"+self.name_collection+".txt"
        name_f_index_inv = "index_inv_"+self.name_collection+".txt"
        
        #On écrit l'index dans un fichier
        with open(name_f_index, 'w') as f1:
            json.dump(self.index, f1)
        #On écrit l'index inversé dans un fichier            
        with open(name_f_index_inv, 'w') as f2:
            json.dump(self.index_inv, f2)
        
        
    def getTfsForDoc(self,doc) :
        #name_f_index = "index_"+self.name_collection+".txt"
        #index = {}
        #with open(name_f_index,'r') as f:
        #   index = json.load(f)
        return self.index[doc.I]
    
    def getTfIDFsForDoc(self,doc) :
        #name_f_index = "index_"+self.name_collection+".txt"
        #index = {}
        #with open(name_f_index,'r') as f:
        #   index = json.load(f)
        docTerms = self.index[doc.I]
        nbDocs = len(self.index)
        docTfIDF = {}
        
        for k_t,v_t in docTerms.items():
            #nb de docs qui contiennent ti
            df = 0
            for k_i,v_i in self.index.items():
                if k_t in v_i :
                    df += 1
                    
            docTfIDF[k_t] = v_t * math.log((1+nbDocs)/(1+df))
        
        return docTfIDF
    
    def getTfsForStem(self, stem) :
        #name_f_index_inv = "index_inv"+self.name_collection+".txt"
        #index_inv = {}
        #with open(name_f_index,'r') as f:
        #   index_inv = json.load(f)
        return self.index_inv[stem]
    
    def getTfIDFsForStem(self, stem) :
        #name_f_index_inv = "index_inv"+self.name_collection+".txt"
        #index_inv = {}
        #with open(name_f_index_inv,'r') as f:
        #   index_inv = json.load(f)
        docs = []
        for k_i,v_i in self.index_inv.items():
            for k_t,v_t in v_i.items():
                if k_t not in docs :
                    docs.append(k_t)
                    
        nbDocs = len(docs)
        stemTfIDF = self.index_inv[stem]
        for k,v in stemTfIDF.items():
            stemTfIDF[k] = v * math.log((1+nbDocs)/(1+len(stemTfIDF)))

        return stemTfIDF
    
    def _get_index(self):
        return self._index
        
    def _set_index(self,newIndex):
        self.index = newIndex
        
    def _get_index_inv(self):
        return self._index_inv
    
    def _set_index_inv(self, newIndexInv):
        self._index_inv = newIndexInv
    
    def _get_index_norm(self):
        return self._index_norm
    
    def _set_index_norm(self,newIndexNorm):
        self._index_norm = newIndexNorm
        
    def _get_index_inv_norm(self):
        return self._index_inv_norm
        
    def _set_index_inv_norm(self,newIndexInvNorm):
        self._index_inv_norm = newIndexInvNorm
        
    
    index = property(_get_index,_set_index)
    index_inv = property(_get_index_inv,_set_index_inv)
    index_norm = property(_get_index_norm,_set_index_norm)
    index_inv_norm = property(_get_index_inv_norm,_set_index_inv_norm)
    
    
    