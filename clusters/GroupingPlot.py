import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from DictofUSStatesAbbr import states_dict

#import data
df = pd.read_csv('../data/data_analysis.tsv', sep='\t')

#preparing for grouping
list_of_states = []
list_to_cluster = []
for index,row in df[['STATE','COST OF LIVING', 'SALARY']].iterrows():
    list_of_states.append(row['STATE'])
    list_to_cluster.append([row['COST OF LIVING'],row['SALARY']])

#reverse the states abbrv dictionary
rev_dict={}
for i,j in states_dict.items():
    rev_dict[j] = i

data = list_to_cluster
print(data)
#特征数为2
estimator = KMeans(n_clusters=4)#构造聚类器，构造一个聚类数为3的聚类器
estimator.fit(data)#聚类
label_pred = estimator.labels_ #获取聚类标签
centroids = estimator.cluster_centers_ #获取聚类中心
inertia = estimator.inertia_ # 获取聚类准则的总和
mark = ['or', 'ob', 'og', 'ok']
color = 0
j=0

for i in label_pred:
    plt.plot([data[j][0]], [data[j][1]], mark[i], markersize = 5)
    plt.text(data[j][0]+2,data[j][1], rev_dict[list_of_states[j]], fontsize=8,)
    j+=1

plt.grid(True, lw = 2, ls = '--', c = '.75')
plt.ylabel('Salary Per Month in USD')
plt.xlabel('COST OF LIVING in Index (100 as Benchmark)')
plt.title('Clustering States Based on Salary and Cost of Living')


#Beautifying
ax=plt.subplot(111)
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

plt.savefig('Clusters.png',bbox_inches='tight')
plt.show()

