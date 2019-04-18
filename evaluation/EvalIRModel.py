# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 17:06:28 2019

@author: Dorian
"""

import numpy as np

class EvalIRModel():
    
    
    def __init__(self,queries,models,evals,labels_models,labels_evals) :
        
        self.queries = queries
        self.models = models
        self.evals = evals 
        
        self.labels_models = labels_models
        self.labels_evals = labels_evals
    
        
    def eval(self) :

        nbQueries = len(self.queries)
                
        dictEval = {}
        dictMoyEcart = {}
        
        for l_m,model in zip(self.labels_models,self.models):
            dictEval[l_m] = {}
            dictMoyEcart[l_m] = {}
            for l_e,evaluation in zip(self.labels_evals,self.evals):
                dictEval[l_m][l_e] = []
                dictMoyEcart[l_m][l_e] = {"moyenne":0.0,"ecart-type":0.0}
                for i,q in self.queries.items() :
                    docsResult = model.getRanking(q.W)
                    
                    idDocs = [ids for ids,score in docsResult]
                    dictEval[l_m][l_e].append(evaluation.evalQuery(idDocs, q))
        
            
        for l_m,ev in dictEval.items():
            for l_e,measures in ev.items():
                moyenne = sum(measures)/nbQueries
                ecart_type = np.sqrt(sum([(xi-moyenne)**2 for xi in measures])/nbQueries)
                                
                                
                dictMoyEcart[l_m][l_e]['moyenne'] = moyenne
                dictMoyEcart[l_m][l_e]['ecart-type'] = ecart_type
                
        """
        for m,l_m in zip(self.models,self.labels_models) :
            
            evals_model = []
            
            for i,q in self.queries.items() :
                
                docsResult = m.getRanking(q.W)
                
                evals_query = np.zeros(nbEvals)
                
                for j in range(nbEvals) :
                    
                    idDocs = [ids for ids,score in docsResult]
                    evals_query.append(evals[j].evalQuery(idDocs, q))
                    
                evals_model.append(evals_query)
                    
            query_evals.append(evals_model)
            
        """
            
        return dictEval,dictMoyEcart
    
    def evalWithPageRank(self, pr) :

        nbQueries = len(self.queries)
                
        dictEval = {}
        dictMoyEcart = {}
        
        for l_m,model in zip(self.labels_models,self.models):
            dictEval[l_m] = {}
            dictMoyEcart[l_m] = {}
            for l_e,evaluation in zip(self.labels_evals,self.evals):
                dictEval[l_m][l_e] = []
                dictMoyEcart[l_m][l_e] = {"moyenne":0.0,"ecart-type":0.0}
                for i,q in self.queries.items() :
                    docsResult = model.getRanking(q.W)
                    idDocsBest = [ids for ids,score in docsResult]
                    
                    docsPageRank = pr.pageRank(idDocsBest,50,4)
                    idDocsPageRank = [ids for ids,score in docsPageRank]

                    dictEval[l_m][l_e].append(evaluation.evalQuery(idDocsPageRank, q))
        
            
        for l_m,ev in dictEval.items():
            for l_e,measures in ev.items():
                moyenne = sum(measures)/nbQueries
                ecart_type = np.sqrt(sum([(xi-moyenne)**2 for xi in measures])/nbQueries)
                                
                                
                dictMoyEcart[l_m][l_e]['moyenne'] = moyenne
                dictMoyEcart[l_m][l_e]['ecart-type'] = ecart_type
                
        """
        for m,l_m in zip(self.models,self.labels_models) :
            
            evals_model = []
            
            for i,q in self.queries.items() :
                
                docsResult = m.getRanking(q.W)
                
                evals_query = np.zeros(nbEvals)
                
                for j in range(nbEvals) :
                    
                    idDocs = [ids for ids,score in docsResult]
                    evals_query.append(evals[j].evalQuery(idDocs, q))
                    
                evals_model.append(evals_query)
                    
            query_evals.append(evals_model)
            
        """
            
        return dictEval,dictMoyEcart
                    
                    