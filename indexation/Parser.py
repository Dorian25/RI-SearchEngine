# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:29:58 2019

@author: Dorian
"""

from .Document import Document

class Parser:
    
    def __init__(self, file_content):
        self.file_content = file_content
        self._documents = []
        
    def parse(self) :
        split_content = self.file_content.split(".I ")
        #on a pas besoin du premier élément (vide)
        new_split_content = split_content[1:]
        
        currentBalise = ""
        contenuBalise = ""
        balises = [".T",".B",".A",".N",".W",".X",".K"]
        
        for doc in new_split_content :
            document = Document()
            
            lines = doc.splitlines()
            document.I = lines[0]
            
            for i in range(1,len(lines)) :
                if lines[i] in balises :
                    if not currentBalise :
                        currentBalise = lines[i]
                    else :
                        if currentBalise == ".T":
                            document.T = contenuBalise
                        elif currentBalise == ".B":
                            document.B = contenuBalise
                        elif currentBalise == ".A":
                            document.A = contenuBalise
                        elif currentBalise == ".N":
                            document.N = contenuBalise
                        elif currentBalise == ".K":
                            document.K = contenuBalise
                        elif currentBalise == ".W":
                            document.W = contenuBalise
                        elif currentBalise == ".X":
                            document.X = contenuBalise
                        else:
                            print("Error")
                        
                        contenuBalise = ""
                        currentBalise = lines[i]
                else :
                    contenuBalise += lines[i]
                    
            currentBalise = ""
            contenuBalise = ""
            self._documents.append(document)
                    
    
    def _get_documents(self):
        return self._documents
    
    def _set_documents(self, new_documents):
        self._documents = new_documents
        
        
    documents = property(_get_documents, _set_documents)