import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN

data = pd.read_csv('hierarchical-clustering.csv')

data = data.dropna(subset=['Annual Income (k$)','Spending Score (1-100)'])

df= data.iloc[:, 3:5].values  #selecting annual income and spending score

plt.scatter(df[:,0], df[:,1], s=10, c="black")
plt.title("Scatter Plot of Data")
plt.xlabel("Annual Income")
plt.ylabel("Spending Score")
plt.show()


wcss = []
for i in range(1,11):
    kmeans = KMeans(n_clusters= i,init = 'k-means++', max_iter= 300, n_init= 10,random_state=42)
    kmeans.fit(df)
    wcss.append(kmeans.inertia_)


plt.plot(range(1,11), wcss,marker='o',linestyle='--')
plt.title("The Elbow Method")
plt.xlabel("Number of clusters")
plt.ylabel("WCSS")
plt.grid()
plt.show()


dbscan = DBSCAN(eps=5, min_samples=5)
labels = dbscan.fit_predict(df)
print(np.unique(labels))

unique_labels = np.unique(labels)
colors = ['blue', 'red', 'green', 'brown', 'pink', 'yellow', 'silver']

# Loop over unique labels and assign colors to clusters
for label in unique_labels:
    # For noise points (-1), color them black
    if label == -1:
        plt.scatter(df[labels == label, 0], df[labels == label, 1], s=10, c='black', label='Noise')
    else:
        # For other clusters, assign colors from the list
        color = colors[label % len(colors)]  # Ensures it works if there are more than 6 clusters
        plt.scatter(df[labels == label, 0], df[labels == label, 1], s=10, c=color, label=f'Cluster {label}')

# Adding labels and legend
plt.xlabel('Annual Income')
plt.ylabel('Spending Score')
plt.legend()
plt.show()
