import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sales = pd.read_csv('./02-Regression_Course/01-LinearRegression/Philadelphia_Crime_Rate_noNA.csv')

plt.figure(figsize=(10, 6))
sns.scatterplot(x=sales["CrimeRate"], y=sales["HousePrice"])
plt.show()
