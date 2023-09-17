# Code block 1: Import libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sb
import matplotlib.pyplot as plt 
import scipy.stats as scp

# Code block 2: Read in data
GlobalSocialIndicators = pd.read_excel('C:\Users\Owner\Desktop\Grad School\Repository\Garrison\data\Python\fatal-police-shootings-data.csv', index_col='Country', na_values=['NA'])
GlobalSocialIndicators.head() # This allows us to inspect the top of the data file