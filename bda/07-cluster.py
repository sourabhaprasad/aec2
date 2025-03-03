import matplotlib.pyplot as plt 
import pandas as pd 
import numpy as np 
import scipy.cluster.hierarchy as shc 
from sklearn.cluster import AgglomerativeClustering 

customer_data = pd.read_csv('hierarchical-clustering.csv') #customerid, gender, age, income, spending score

customer_data.shape
customer_data.head()

data = customer_data.iloc[:, 3:5].values  #selecting annual income and spending score
data

plt.figure(figsize=(10, 7))
plt.title("Customer Dendrogram")
shc.dendrogram(shc.linkage(data, method='ward'))
plt.show()


cluster = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward') 
# affinity = 'euclidean'
labels_ = cluster.fit_predict(data)

plt.figure(figsize=(10, 7))
plt.scatter(data[:, 0], data[:, 1], c=labels_, cmap='rainbow')
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.title("Clusters of Customers")
plt.show()