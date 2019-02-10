# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:27:58 2019

@author: Dorian
"""

from indexation.Document import Document
from indexation.Parser import Parser
from indexation.IndexerSimple import IndexerSimple


file_cacm = open("data/cacm/cacm.txt","r")
content_cacm = file_cacm.read()

file_cisi = open("data/cisi/cisi.txt","r")
content_cisi = file_cisi.read()

parse_cacm = Parser(content_cacm)
parse_cacm.parse()
documents_cacm = parse_cacm.documents


parse_cisi = Parser(content_cisi)
parse_cisi.parse()
documents_cisi = parse_cisi.documents

"""for d in documents_cacm :
    print("I"+d.I)
    print("T"+d.T)
    print("B"+d.B)
    print("N"+d.N)
    print("A"+d.A)
    print("W"+d.W)
    print("X"+d.X)
    print("K"+d.K)
    print("##########################")
"""
          
index_cacm = IndexerSimple("cacm")
index_cacm.indexation(documents_cacm)

index_cisi = IndexerSimple("cisi")
index_cisi.indexation(documents_cisi)

#print(index_cacm.getTfsForDoc(documents_cacm[5]))
#print(index_cacm.getTfIDFsForDoc(documents_cacm[0]))
#print(index_cacm.getTfsForStem("report"))
#print(index_cacm.getTfIDFsForStem("preliminari"))