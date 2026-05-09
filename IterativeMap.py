# -*- coding: utf-8 -*-
"""
Created on Mon May  4 17:51:59 2026

@author: matth
"""

import numpy as np
import matplotlib.pyplot as plt

class IterativeMap:
    """
        A class for evolving and plotting iterative maps as described in 
        "Dynamics of Complex systems" by Yaneer Bar-yam.
    """
    
    def __init__(self,mixing_alpha=1):
        self.mixing_alpha = mixing_alpha
        
        
    def quadratic_map(self,state,scaling_param):
        return scaling_param*state*(1-state)
    
    def velocity_map(self,state,velocity):
        return state+velocity
    
    def growth_map(self,state,growth_rate):
        return growth_rate*state
    
    def iterate(self,func,state,k_max,*args):
        idx = 0
        state_lst = []
        while idx < k_max:
            state = state*(1-self.mixing_alpha)+self.mixing_alpha*func(state,*args)
            state_lst.append(state)
            idx += 1
            
        return state_lst
            
    def identity_map(self,state):
        return state
        
    def iterative_plot(self,func,state,k_max,*args):
        s_vs_t = self.iterate(func,state,k_max,*args)
        s0_range = np.linspace(0,1)
        f_s = [func(state,*args) for state in s0_range]
        f2_s = [func(func(state,*args),*args) for state in s0_range]
        
        fig,ax = plt.subplots(1,3)
        ax[0].scatter([t for t in range(k_max)],s_vs_t)
        ax[1].plot(s0_range,s0_range)
        ax[1].plot(s0_range,f_s)
        ax[2].plot(s0_range,s0_range)
        ax[2].plot(s0_range,f2_s)
        plt.tight_layout()
        return f_s
        
        
    
    