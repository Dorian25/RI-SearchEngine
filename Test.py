# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:27:58 2019

@author: Dorian
"""

from indexation.Document import Document
from indexation.Parser import Parser
from indexation.IndexerSimple import IndexerSimple
from ordonnancement.Weighter1 import Weighter1
from ordonnancement.Weighter2 import Weighter2
from ordonnancement.Weighter3 import Weighter3
from ordonnancement.Weighter4 import Weighter4
from ordonnancement.Weighter5 import Weighter5
from ordonnancement.IRModel import IRModel
from ordonnancement.Okapi import Okapi
from ordonnancement.ModeleLangue import ModeleLangue
from ordonnancement.Vectoriel import Vectoriel

file_cacm = open("data/cacm/cacm.txt","r")
content_cacm = file_cacm.read()

file_cisi = open("data/cisi/cisi.txt","r")
content_cisi = file_cisi.read()

parse_cacm = Parser(content_cacm)
documents_cacm = parse_cacm.parse()

#parse_cisi = Parser(content_cisi)
#documents_cisi = parse_cisi.parse()
          
index_cacm = IndexerSimple("cacm")
index_cacm.indexation(documents_cacm)

#index_cisi = IndexerSimple("cisi")
#index_cisi.indexation(documents_cisi)

#w = Weighter1(index_cacm)
w = Weighter5(index_cacm)
#print(w.getWeightsForDoc("54"))
v = Vectoriel(index_cacm,w,False)
print(v.getRanking("home top sales homes"))

#print(index_cacm.getTfsForDoc(documents_cacm[5]))
#print(index_cacm.getTfIDFsForDoc(documents_cacm[0]))
#print(index_cacm.getTfsForStem("report"))
#print(index_cacm.getTfIDFsForStem("preliminari"))