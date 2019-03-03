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
        
    def parse(self) :
        
        requetes = {}
        
        if not self._req_content :
            print("Error. Le contenu est vide.")
        else :
            split_content_req = self._req_content.split(".I ")
            split_content_pert = self._pertinence_content.splitlines()
            #on a pas besoin du premier élément (vide)
            new_split_content = split_content_req[1:]
            
            currentBalise = ""
            contenuBalise = ""
            balises = [".A",".N",".W"]
            
            for req in new_split_content :
                query = Query()
                
                lines = req.splitlines()
                query.I = lines[0]
                
                for i in range(1,len(lines)) :
                    if lines[i] in balises :
                        if not currentBalise :
                            currentBalise = lines[i]
                        else :
                            if currentBalise == ".A":
                                query.A = contenuBalise
                            elif currentBalise == ".N":
                                query.N = contenuBalise
                            elif currentBalise == ".W":
                                query.W = contenuBalise
                            else:
                                print("Error")
                            
                            contenuBalise = ""
                            currentBalise = lines[i]
                    else :
                        contenuBalise += lines[i]
                        
                currentBalise = ""
                contenuBalise = ""
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