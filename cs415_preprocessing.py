import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/breast-cancer-wisconsin/breast-cancer-wisconsin.data', header=None)

data.columns = ['Sample code', 'Clump Thickness', 'Uniformity of Cell Size','Uniformity of Cell Shape', 'Marginal Adhesion', 'Single Epithelial Cell Size', 'Bare Nuclei', 'Bland Chromatin', 'Normal Nucleoli', 'Mitoses','Class']

data = data.drop(['Sample code'],axis=1)

#! Missing Data in the dataset are represented by "?", so we change it to NaN
data = data.replace('?',np.NaN)

print('Number of instances = %d' % (data.shape[0]))
print('Number of attributes = %d' % (data.shape[1]))

for col in data.columns:
    print(f"{col}: {data[col].isna().sum()}")


# ! editing column "Bare Nuclei"

data2 = data['Bare Nuclei']
print('Before replacing missing values:')
print(data2[20:25])

data2 = data2.fillna(data2.median())

print('\nAfter replacing missing values:')
print(data2[20:25])

#! Discarding records with dataset

print('Number of rows in original data = %d' % (data.shape[0]))

data2 = data.dropna()

print('Number of rows after discarding missing values = %d' % (data2.shape[0]))

#! Outliners

data2 = data.drop(['Class'],axis=1)
data2['Bare Nuclei'] = pd.to_numeric(data2['Bare Nuclei'])
fig = plt.figure(figsize =(20, 3))
 
Z = (data2-data2.mean())/data2.std()
print(Z[20:25])