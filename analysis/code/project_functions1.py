import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random
import scipy.stats as stats

def loadAndProcess(csv):
    """Loads and processes data for this specific analysis question (analysis 1)

    Args:
        csv (str): Path to csv
    """
    
    # My method is written differently from the sample method since I wanted to drop columns before removing NaN values
    
    random.seed(68504364)
    
    rawData = pd.read_csv(csv)
    modifiedData =\
        rawData.drop(["Primary streaming service","Fav genre","Timestamp","Age","Exploratory","Foreign languages","BPM","Frequency [Classical]","Frequency [Country]","Frequency [EDM]","Frequency [Folk]","Frequency [Gospel]","Frequency [Hip hop]","Frequency [Jazz]","Frequency [K pop]","Frequency [Latin]","Frequency [Lofi]","Frequency [Metal]","Frequency [Pop]","Frequency [R&B]","Frequency [Rap]","Frequency [Rock]","Frequency [Video game music]","Music effects","Permissions"], axis = 1)\
        .dropna().reset_index(drop = True)\
        .assign(total_score = rawData["Anxiety"] + rawData["OCD"] + rawData["Depression"] + rawData["Insomnia"])\
        .rename(columns = {"Hours per day" : "HPD"})\
        .rename(columns = {"While working" : "WW"})\
    # add jitter to the Hours per Day
    jitteredHPD = pd.Series()
    for i in range(0,len(modifiedData["HPD"])):
        jitteredHPD.at[i] = modifiedData["HPD"][i] + (random.random() * 0.2 - 0.1)  # adds a value of [-0.1,0.1)
    modifiedData = modifiedData.assign(JHPD = jitteredHPD)
    
    return modifiedData

def rAndPValue(data, y, x, **kws):
    r, p = stats.pearsonr(data[y], data[x])
    ax = plt.gca()
    ax.text(.05, .8, 'r = {:.4f}, p = {:.4f}'.format(r, p),
            transform=ax.transAxes)