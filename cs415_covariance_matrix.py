import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# # download the wine dataset
# df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/wine/wine.data", header=None)


# df = df.drop(columns=[0])

# print(df.head())

# df.columns = ["C"+str(i) for i in range(1, len(df.columns)+1)]

# mean_c1 = np.mean(df.C1)
# mean_c2 = np.mean(df.C2)
# temp = 0

# for c1, c2 in zip(df.C1, df.C2):
#     temp += (c1 - mean_c1)*(c2 - mean_c2)
    
# cov = temp/(len(df) - 1)

# print(df.cov())

df = pd.DataFrame({"A": [1,2,4,2,5],
                   "B": [100, 300, 200, 600, 100],
                   "C": [10, 15, 20, 10, 30]})

new_Val = [4, 500, 40]

print(df.cov())
invcov = np.linalg.inv(df.cov())
mean = []

[mean.append(np.mean(y)) for x,y in df.iteritems()]

distance = [x - y for x,y in zip(new_Val, mean)]

print(distance)
# print(f"The distance is {mean}")
part1 = np.dot(distance, invcov)

print(np.dot(distance, invcov))

part2 = np.dot(part1, distance)

print(part2)

print(np.sqrt(part2))