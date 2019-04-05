#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 14:46:02 2019

@author: Dorian
@author: Mouhamad
"""


from .Query import Query

class QueryParser:

    def __init__(self, req_content, pertinence_content):
        self._req_content = req_content
        self._pertinence_content = pertinence_content
        
    def remplirQuery(self,query, contenuBalise, currentBalise) :
        if currentBalise == ".A":
            query.A = " ".join(contenuBalise)
        elif currentBalise == ".N":
            query.N = " ".join(contenuBalise)
        elif currentBalise == ".W":
            query.W = " ".join(contenuBalise)
        else:
            print("Error")
        
        
    def parse(self) :
        
        requetes = {}
        
        if not self._req_content :
            print("Error. Le contenu est vide.")
        else :
            split_content_req = self._req_content.split(".I ")
            split_content_pert = self._pertinence_content.splitlines()
            #on a pas besoin du premier élément (vide)
            new_split_content = split_content_req[1:]
            
            balises = [".A",".N",".W"]
            
            for req in new_split_content :
                query = Query()
                
                currentBalise = ""
                contenuBalise = []
                
                lines = req.splitlines()
                query.I = lines[0]
                
                for i in range(1,len(lines)) :
                    if lines[i] in balises :
                        if not currentBalise :
                            currentBalise = lines[i]
                        else :
                            self.remplirQuery(query,contenuBalise,currentBalise)
                            contenuBalise = []
                            currentBalise = lines[i]
                    else :
                        contenuBalise.append(lines[i])
                #on affecte le contenu pour la derniere balise
                self.remplirQuery(query,contenuBalise,currentBalise)
                requetes[query.I] = query
            
            for line in split_content_pert :
                tokens = line.split()
                idReq = int(tokens[0])
                idDocPert = tokens[1]
                requetes[str(idReq)].listDocsPertinents.append(idDocPert)
            
            return requetes
    
    def _get_req_content(self):
        return self._req_content
    
    def _set_req_content(self, newContent):
        self._req_content = newContent
        
    def _get_pert_content(self):
        return self._pertinence_content
    
    def _set_pert_content(self, newContent):
        self._pertinence_content = newContent
    
    req_content = property(_get_req_content, _set_req_content)
    
    pertinence_content = property(_get_pert_content, _set_pert_content)