import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

data = pd.read_csv('final_data.csv')
print(data.head(5))

print(data.columns)

data = data[['bathrooms', 'bedrooms', 'finishedsqft', 'lastsoldprice', 'zestimate']]
print(data.head(5))

print(data[['bathrooms', 'bedrooms']].cov())

print(data[['bathrooms', 'bedrooms']].var())

print(data[['bathrooms', 'bedrooms']].corr())

print(data[['bathrooms', 'bedrooms']].corr('spearman'))

print(data.corr())

print(data.corr('spearman'))

plt.figure(figsize=(8, 6))
sns.heatmap(data.corr('spearman'))
plt.show()