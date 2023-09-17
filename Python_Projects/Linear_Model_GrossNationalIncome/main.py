# Code block 1: Import libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import seaborn as sb
import matplotlib.pyplot as plt 
import scipy.stats as scp

# Code block 2: Read in data
GlobalSocialIndicators = pd.read_excel('http://data.shortell.nyc/files/HumanDevelopment.xlsx', index_col='Country', na_values=['NA'])
GlobalSocialIndicators.head() # This allows us to inspect the top of the data file
GlobalSocialIndicators[['Human Development Index (HDI)', 'Gross National Income (GNI) per Capita']].describe()
GlobalSocialIndicators.describe()

# Code block 3: The linear model
Y = GlobalSocialIndicators['Life Expectancy at Birth']
X = GlobalSocialIndicators['Gross National Income (GNI) per Capita']
X = sm.add_constant(X)
model0 = sm.OLS(Y, X, missing='drop').fit()
print(model0.summary())

# Code block 4: Visualizing the linear model
p = sb.lmplot('Gross National Income (GNI) per Capita', 'Life Expectancy at Birth', data=GlobalSocialIndicators)
p.fig.set_figwidth(20)
p.fig.set_figheight(12)
plt.show()

# Code block 5: The linear model
Y = GlobalSocialIndicators['Life Expectancy at Birth']
X = GlobalSocialIndicators[['Gross National Income (GNI) per Capita', 'Expected Years of Education']]
X = sm.add_constant(X)
model2 = sm.OLS(Y, X, missing='drop').fit()
print(model2.summary())

# Checking on colinearity
corrtab, corrsig = scp.stats.pearsonr(GlobalSocialIndicators['Gross National Income (GNI) per Capita'], GlobalSocialIndicators['Mean Years of Education'])
corrtab
corrsig