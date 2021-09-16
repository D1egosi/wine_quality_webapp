# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 17:14:01 2021

@author: Cognitive-02
"""

# import

import os
import pandas as pd
import pickle

from wine_quality.WineQuality import WineQuality

from flask import Flask, request


# load model
model = pickle.load(open( 'model/model_wine_quality.pkl', 'rb' ))

# instanciate  flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    test_json = request.get_json()
    
    # collect data
    if test_json:
        if isinstance(test_json, dict): # unique value
            df_raw = pd.DataFrame(test_json.index[0])
        else:
            df_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
        
         # iniciando a preparação dos dados 
    pipeline = WineQuality()
         
    df1 = pipeline.data_preparation(df_raw)
    

        # prediction
        
        
    pred = model.predict(df1)
        
    df1['prediction'] = pred
        
    return df1.to_json( orient='records' )

if __name__ == '__main__':
    #star flask
    port = os.environ.get('PORT', 5000)
    app.run(host='0.0.0.0', port=port)

