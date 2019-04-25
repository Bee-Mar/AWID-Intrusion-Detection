#!/usr/bin/env python3
from os import cpu_count
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.neighbors import KNeighborsClassifier

resource_dir = Path('./', 'resources')

# Read in preprocessed AWID dataset
data = pd.read_csv(
    Path(resource_dir, 'preproc_dataset.zip'), sep=',', compression='zip')

# How to normalize the 'wlan_mgt.fixed.capabilities.privacy' column
# for each value in column, convert to decimal inplace
# decimal_value = int(hex_value, 16) (hex_value must be treated as string)
# Then do MinMax Normalization
# privacy = data[['wlan_mgt.fixed.capabilities.privacy']].values.astype(float)
# data['wlan_mgt.fixed.capabilities.privacy'] = scaler.fit_transform(privacy)


# my code from lab 4 where I used KNN. Variable names need to be changed
'''
# to run the KMeans and DBSCAN with parallel jobs
cpu_core_cnt = cpu_count()

# producing elbow plot to determine K value
for i in range(len(dists)):
    for j in range(1, 15):
        km = KMeans()
        km.init = 'k-means++'
        km.random_state = 0
        km.n_clusters = j
        km.n_jobs = cpu_core_cnt
        km = km.fit(coords[i])
        dists[i].append(km.inertia_)

for i in range(len(dists)):
    plot.plot(range(1, 15), dists[i])
    plot.xticks(np.arange(1, 15, step=1))
    plot.title('Elbow Plot - ' + categories[i])
    plot.xlabel('K-Value')
    plot.ylabel('Aggregate Distance')
    plot.show()

# after viewing the elbow graph, 3 clusters appears to be optimal for all

kmeans_clusters = [[], [], [], [], []]

# initializing to zero
kmeans_acc = [0.0, 0.0, 0.0, 0.0, 0.0]

true_labels = [
    all_true_labels,
    burg_df['CATEGORY'],
    motor_df['CATEGORY'],
    other_df['CATEGORY'],
    street_df['CATEGORY'],
]

kmeans_labels = [[], [], [], [], []]

print('--------------')
print('KMEANS RESULTS')
print('--------------')
for i in range(5):
    kmeans = KMeans()
    kmeans.n_clusters = 3
    kmeans.n_jobs = cpu_core_cnt
    kmeans_labels[i] = kmeans.fit_predict(coords[i])
    kmeans_clusters[i] = list(np.unique(kmeans_labels[i]))
    kmeans_acc[i] = cluster_acc(kmeans_clusters[i], kmeans_labels[i],
                                true_labels[i])

display_accuracy(kmeans_acc[ALL], kmeans_clusters[ALL], categories[ALL])

make_cluster_plots(categories, kmeans_clusters, kmeans_labels, coords,
                   'KMeans')
'''
