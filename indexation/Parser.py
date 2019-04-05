# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:29:58 2019

@author: Dorian
@author: Mouhamad
"""

from .Document import Document

class Parser:
    
    def __init__(self, file_content):
        self._file_content = file_content
        
    def remplirDoc(self,document,contenuBalise,currentBalise) :
        if currentBalise == ".T":
            document.T = " ".join(contenuBalise)
        elif currentBalise == ".B":
            document.B = " ".join(contenuBalise)
        elif currentBalise == ".A":
            document.A = " ".join(contenuBalise)
        elif currentBalise == ".N":
            document.N = " ".join(contenuBalise)
        elif currentBalise == ".K":
            document.K = " ".join(contenuBalise)
        elif currentBalise == ".X":
            document.X = " ".join(contenuBalise)
        elif currentBalise == ".W":
            document.W = " ".join(contenuBalise)
        else:
            print("Error")
        
    def parse(self) :
        
        documents = {}
        
        if not self._file_content :
            print("Error. Le contenu est vide.")
        else :
            split_content = self.file_content.split(".I ")
            #on a pas besoin du premier élément (vide)
            new_split_content = split_content[1:]
       
            balises = [".T",".B",".A",".N",".W",".X",".K"]
            
            for doc in new_split_content :
                document = Document()
                
                currentBalise = ""
                contenuBalise = []
                
                lines = doc.splitlines()
                document.I = lines[0]
                
                for i in range(1,len(lines)) :
                    if lines[i] in balises :
                        if not currentBalise :
                            currentBalise = lines[i]
                        else :
                            self.remplirDoc(document,contenuBalise,currentBalise)
                            contenuBalise = []
                            currentBalise = lines[i]
                    else :
                        contenuBalise.append(lines[i])
                #on affecte le contenu pour la derniere balise        
                self.remplirDoc(document,contenuBalise,currentBalise)        
                documents[document.I] = document
            
            return documents
    
    def _get_file_content(self):
        return self._file_content
    
    def _set_file_content(self, newContent):
        self._file_content = newContent
    
    file_content = property(_get_file_content, _set_file_content)