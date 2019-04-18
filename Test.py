# -*- coding: utf-8 -*-
"""
Created on Sun Feb 10 11:27:58 2019

@author: Dorian
@author: Mouhamad
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
from evaluation.QueryParser import QueryParser
from evaluation.Query import Query
from evaluation.EvalMesurePrecision import EvalMesurePrecision
from evaluation.EvalMesurePrecisionMoyenne import EvalMesurePrecisionMoyenne
from evaluation.EvalMesureReciprocalRank import EvalMesureReciprocalRank
from evaluation.EvalMesureRappel import EvalMesureRappel
from evaluation.EvalMesureFMeasure import EvalMesureFMeasure
from evaluation.EvalMesureNDCG import EvalMesureNDCG
from evaluation.EvalIRModel import EvalIRModel
from evaluation.PageRank import PageRank


"""
docs = ["the new home has been saled on top forecasts",
       "the home sales rise in july",
       "there is an increase in home sales in july",
       "july encounter a new home sales rise"]

d1 = Document()
d1.I = '1'
d1.T = docs[0]
d2 = Document()
d2.I = '2'
d2.T = docs[1]
d3 = Document()
d3.I = '3'
d3.T = docs[2]
d4 = Document()
d4.I = '4'
d4.T = docs[3]

queries = ["top sales","sales increase july", "new home"]

q1 = Query()
q1.I = '1'
q1.W = queries[0]
q1.listDocsPertinents = ['1']
q2 = Query()
q2.I = '2'
q2.listDocsPertinents = ['2','3']
q2.W = queries[1]
q3 = Query()
q3.I = '3'
q3.W = queries[2]
q3.listDocsPertinents = []

ex_doc = {d1.I:d1,d2.I:d2, d3.I:d3,d4.I:d4 }
index_ex = IndexerSimple("exemp")
index_ex.indexation(ex_doc)

ex_query = {q1.I:q1,q2.I:q2, q3.I:q3 }


#w = Weighter5(index_ex)
#v = Vectoriel(index_ex,w,False)
ml = ModeleLangue(index_ex)
oka = Okapi(index_ex)

precision = EvalMesurePrecision() 
rappel = EvalMesureRappel()
fmeasure = EvalMesureFMeasure()

evaluations,moyecart = EvalIRModel(ex_query,[ml,oka],[precision,rappel,fmeasure],["Modele Langue","Okapi_BM25"],["Precision","Rappel","FMeasure"]).eval()
"""

file_cacm = open("data/cacm/cacm.txt","r")
content_cacm = file_cacm.read()
#file_cisi = open("data/cisi/cisi.txt","r")
#content_cisi = file_cisi.read()

parse_cacm = Parser(content_cacm)
documents_cacm = parse_cacm.parse()
#parse_cisi = Parser(content_cisi)
#documents_cisi = parse_cisi.parse()
          
index_cacm = IndexerSimple("cacm")
index_cacm.indexation(documents_cacm)
#index_cisi = IndexerSimple("cisi")
#index_cisi.indexation(documents_cisi)

query_cacm = open("data/cacm/cacm.qry","r")
pertinence_cacm = open("data/cacm/cacm.rel","r")

content_cacm_q = query_cacm.read()
content_cacm_pert = pertinence_cacm.read()

parse_cacm_q = QueryParser(content_cacm_q,content_cacm_pert)
requetes_cacm = parse_cacm_q.parse()

#modèles
ml = ModeleLangue(index_cacm)
oka = Okapi(index_cacm)
w = Weighter5(index_cacm)
v = Vectoriel(index_cacm,w,False)

#métriques
precision = EvalMesurePrecision() 
rappel = EvalMesureRappel()
fmeasure = EvalMesureFMeasure()
reciprocal_rank = EvalMesureReciprocalRank()
ndcg = EvalMesureNDCG()
precision_moy = EvalMesurePrecisionMoyenne()

#comparaison modèles avec métriques
pRank = PageRank(index_cacm)
evaluations,moyecart = EvalIRModel(requetes_cacm,[ml,v],[precision,rappel,fmeasure,ndcg],["Modele Langue","Vectoriel_W5"],["Precision","Rappel","FMeasure","NDCG"]).eval()
evaluations_pr,moyecart_pr = EvalIRModel(requetes_cacm,[ml,v],[precision,rappel,fmeasure,ndcg],["Modele Langue","Vectoriel_W5"],["Precision","Rappel","FMeasure","NDCG"]).evalWithPageRank(pRank)