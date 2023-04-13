import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import random

def loadd(csv):
    dataload_1 = pd.read_csv(csv)
    dataload = dataload_1[["Age", "Primary streaming service", "Hours per day", "Fav genre","BPM", "Exploratory", "Foreign languages"]]
    dataload.dropna()
    return dataload