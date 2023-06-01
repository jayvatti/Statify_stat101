#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 21:53:10 2023

@author: jayvatti
"""

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt

from ErrorStat import PlotError

import copy

class Plots:
    def dotPlot(self, data, label_y = "Frequency"):
        np.random.seed(42)
        try:
            df = pd.DataFrame(copy.deepcopy(data))
            sns.stripplot(jitter= True,data=df, orient='h', dodge=True)
            plt.ylabel(label_y)
            plt.show()
        except PlotError as e:
            print('ERROR:', e.error, e.args[-1], e.plot, sep=': ')
    
    def boxPlot(self,data, title,label_x,label_y):
        keys = list(data.keys())
        values = list(data.values())
    
        fig, ax = plt.subplots()
        
        ax.boxplot(values, patch_artist=True, vert=False)
        ax.set_yticklabels(keys)
        
        ax.set_title(title)
        ax.set_xlabel(label_x)
        ax.set_ylabel(label_y)
            
        plt.show()
    
    def histogram(self,data,label_y = 'Frequency', bins = 0):
        try:
            if len(data.keys()) < 2:
                raise PlotError('{COLS < 2}','Not Enough Columns', 'Histogram')
            for i in data.keys():
                npArray = np.array(data[i])
                sturge = int(np.ceil(np.log2(len(npArray)) + 1))
                bin_value = bins
                if bins == 0: bin_value = sturge
                else: bin_value = bins 
                plt.hist(npArray, bin_value, color='lightgray', edgecolor='black')
                plt.ylabel(label_y)
                plt.title(i)
                plt.show()
                
        except PlotError as e:
            print('ERROR:',e.error,e.args[-1],e.plot,sep=': ')
            
      
    def scatterPlot(self,column_dict,order, label_x, label_y, regression):
        try:
            if len(column_dict.keys()) < 2:
                raise PlotError('{COLS < 2}','Not Enough Columns', 'Scatter_Plot')

            plt.scatter(column_dict[order[0]], column_dict[order[1]])

            plt.xlabel(label_x)
            plt.ylabel(label_y)
            
            if regression == True:
                slope, intercept = np.polyfit(column_dict[order[0]], column_dict[order[1]], 1)
                regression_line = slope * np.array(column_dict[order[0]]) + intercept
                plt.plot(column_dict[order[0]], regression_line, color='red', label='Linear Regression')

            plt.show()
        except PlotError as e:
            print('ERROR:',e.error,e.args[-1],e.plot,sep=': ')

