import numpy as np
import pandas as pd
import statistics
import seaborn as sns
from matplotlib import pyplot as plt
from scipy import stats


def space_delimiter(fileName):
    try:
       with open(fileName) as infile:
           data = infile.read().replace(' ', ',')
           print(data, file=open('data.csv', 'w'))
    except Exception as e:
        print(f"{fileName} does not EXIST!")
        print(f"Exception: {e}",end="\n\n")
    
def read_csv(fileName):
    try:
        csv_file = pd.read_csv(fileName)
        data_dict = csv_file.to_dict(orient='list')
        print(data_dict)
        return data_dict
    except Exception as e:
        print(f"{fileName} does not EXIST!")
        print(f"Exception: {e}",end="\n\n")
        return {"INVALID":[0,0]}

def mdfy_dict(dictionary,columns = [""]):
    temp = dictionary.copy()
    for i in dictionary.keys():
        if i not in columns: temp.pop(i)
    return temp

def dotPlot(dictionary):
    df = pd.DataFrame(dictionary)
    sns.stripplot(data=df, jitter=True, orient='h',dodge='True')
    plt.ylabel('Frequency')
    plt.show()

def boxPlot(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    
    fig, ax = plt.subplots()
    
    ax.boxplot(values, patch_artist=True, vert=False)
    ax.set_yticklabels(keys)
    
    ax.set_title('Box-Whisker Plot')
    ax.set_xlabel('Values')
    ax.set_ylabel('Groups')
        
    plt.show()
 
def histogram(dictionary):
    for i in dictionary.keys():
        npArray = np.array(dictionary[i])
        sturge = int(np.ceil(np.log2(len(npArray)) + 1))
        plt.hist(npArray, bins=sturge, color='lightgray', edgecolor='black')
        plt.ylabel('Frequency')
        plt.title(i)
        plt.show()
  
def scatterPlot(dictionary):
    axis = list(dictionary.keys())
    data = [value for value in dictionary.values()]

    plt.scatter(data[1], data[0])

    plt.xlabel(axis[1])
    plt.ylabel(axis[0])
    plt.show()
  
def linearRegres(dictionary,indexes):
    result = stats.linregress(dictionary[indexes[0]], dictionary[indexes[1]])
    print("LINEAR REGRESSION:")
    print(f'Slope:      {result.slope}')
    print(f'Intercept:  {result.intercept}')
    print(f'r:          {result.rvalue}', end ="\n\n")
    print(f'EQUATION:   y = {result.slope:.6f}x + {result.intercept:.6f}',end="\n\n")
    print("--------------------\n")
    
    
def datasetSummary(**kwargs):
    if len(kwargs) > 1: 
        linearRegres(kwargs, ["x","y"])
        scatterPlot(kwargs)
    dotPlot(kwargs)
    boxPlot(kwargs)
    histogram(kwargs)
    
    for i in kwargs.keys():
        print(f"SUMMARY OF '{i}':",end="\n\n")
        kwargs[i].sort()
        print("this graph is 'SKEWED RIGHT'") if (statistics.mean(kwargs[i]) > statistics.median(kwargs[i])) else print("this graph is 'SKEWED LEFT'")
        print("\n")
        data = np.array(kwargs[i])
        x = pd.Series(data)
        print(f'var      {statistics.variance(kwargs[i])}')
        print(f'10%mean  {stats.trim_mean(kwargs[i], 0.1)}')
        quartiles = np.percentile(data, [25, 50, 75])
        IQR = quartiles[2] - quartiles[0]
        print(f'IQR      {IQR}')
        print(f'summary  ({min(kwargs[i])},{quartiles[0]},{quartiles[1]},{quartiles[2]},{max(kwargs[i])})',end="\n\n")
        print(f'uf       {quartiles[2] + (1.5*IQR)}')
        print(f'lf       {quartiles[0] - (1.5*IQR)}',end='\n\n')
        print(x.describe(),end='\n---------------------\n\n')



updated_dict = mdfy_dict(read_csv('data.csv'),["x","y"])
datasetSummary(**updated_dict)



