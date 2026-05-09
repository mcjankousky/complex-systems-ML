# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:40:48 2026

@author: matth
"""

import numpy as np
from itertools import product
import pandas as pd
from sklearn.model_selection import train_test_split

class GenerateToyData:
    """
        A class for generating some data for toy models to evaluate capabilities
        of different ML algorithms, pipelines, and approaches. generate_mod_data
        creates a dataframe with modulo arithmetic. This is the simplest example
        of periodic data. Approaches that perform poorly on this data are
        expected to perform poorly in any case that contains periodic data.
    """
    
    def __init__(self):
        self.df = pd.DataFrame()
        self.df_train = pd.DataFrame()
        self.df_test = pd.DataFrame()

    def generate_mod_data(self,quotient=10000,mod_n=10):
        mod_array = np.zeros((quotient,mod_n))
        
        for x,y in product(range(quotient),range(mod_n)):
            mod_array[x][y] = x%(y+1)
            
        self.df = pd.DataFrame(mod_array,index=[x for x in range(quotient)],columns=[x+1 for x in range(mod_n)])

    def save_data(self,columns,prefix,test_size=0.2):
        
        self.df[columns].to_pickle('{}_df.p'.format(prefix))
        
        self.df_train,self.df_test = train_test_split(self.df[columns],test_size=test_size,random_state=42)
        
        self.df_train.to_pickle('{}_df_train.p'.format(prefix))
        
        self.df_test.to_pickle('{}_df_test.p'.format(prefix))
        
        # TODO: Add sparse option for all - considering not only sampling from 
        # subset of rows, but also from subset of columns

