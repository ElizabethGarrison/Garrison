import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

# Read the data into a DataFrame
GlobalSocialIndicators = pd.read_excel('http://data.shortell.nyc/files/HumanDevelopment.xlsx', index_col='Country', na_values=['NA'])

# Display the first few rows of the DataFrame to inspect the data
GlobalSocialIndicators.head()

# Define the dependent variable (DV) and independent variable (IV)
Y = GlobalSocialIndicators['Life Expectancy at Birth']
X = GlobalSocialIndicators['Gross National Income (GNI) per Capita']

# Add a constant term to the independent variable (intercept)
X = sm.add_constant(X)

# Fit the linear regression model
model = sm.OLS(Y, X).fit()

# Print the regression summary
print(model.summary())

# Scatter plot of the data
plt.scatter(X['Gross National Income (GNI) per Capita'], Y, label='Data')

# Plot the regression line
plt.plot(X['Gross National Income (GNI) per Capita'], model.predict(X), color='red', label='Regression Line')

# Add labels and a legend
plt.xlabel('Gross National Income (GNI) per Capita')
plt.ylabel('Life Expectancy at Birth')
plt.legend()

# Show the plot
plt.show()