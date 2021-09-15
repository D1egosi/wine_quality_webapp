# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 17:18:22 2021

@author: Cognitive-02
"""

## criiando uma classe com o nome do modelo - WineQuality

import pickle

class WineQuality(object):
    def __init__(self):  
        #construtor para iniciar a classe com o self trazendo os scalers para uso no modelo padronizar dados
        self.free_sulfur_scaler = pickle.load(open('parameter/free_sulfur_scaler.pkl','rb'))
        self.total_sulfur_scaler = pickle.load(open('parameter/total_sulfur_scaler.pkl','rb'))
        
   
    
    def data_preparation( self, df ):
        
        #rescaling coluna free sulfur 
        df['free sulfur dioxide'] = self.free_sulfur_scaler.transform(df[['free sulfur dioxide']].values)
        
        #rescaling coluna total sulfur 
        df['total sulfur dioxide'] = self.total_sulfur_scaler.transform(df[['total sulfur dioxide']].values)
        
        return df
    
    