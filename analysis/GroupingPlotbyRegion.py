
def cluster_region(params='region'):
    '''
    This function creates region-based scatter-plot. It can also be used to create a cluster plot.
    Args:
        params (str): when the string equals to 'region', the function shows a region-based scatter-plot, when it equals to 'cluster', the function shows a cluster plot.
    '''
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    from sklearn.cluster import KMeans
    from DictofUSStatesAbbr import states_dict
    from GroupingRegion import region_color, region_dict

    #import data
    df = pd.read_csv('../data/data_analysis.tsv', sep='\t')

    #preparing for grouping
    list_of_states = []
    list_to_cluster = []
    list_of_colors = []
    for index,row in df[['STATE','CODE','COST OF LIVING', 'SALARY']].iterrows():
        list_of_states.append(row['STATE'])
        list_to_cluster.append([row['COST OF LIVING'],row['SALARY']])
        for key, value in region_dict.items():
            if row['CODE'] in value:
                list_of_colors.append(region_color[key])

    #reverse the states abbrv dictionary
    rev_dict={}
    for i,j in states_dict.items():
        rev_dict[j] = i

    data = list_to_cluster
    #特征数为2
    estimator = KMeans(n_clusters=4)#构造聚类器，构造一个聚类数为3的聚类器
    estimator.fit(data)#聚类
    label_pred = estimator.labels_ #获取聚类标签
    centroids = estimator.cluster_centers_ #获取聚类中心
    inertia = estimator.inertia_ # 获取聚类准则的总和
    color = 0
    mark = ['or', 'ob', 'og', 'ok']
    j=0

    if params=='region':
        for i in label_pred:
            plt.plot([data[j][0]], [data[j][1]], list_of_colors[j], markersize = 5)
            plt.text(data[j][0]+2,data[j][1], rev_dict[list_of_states[j]], fontsize=8,)
            j+=1
        plt.title('ScatterPlotBased on Region')

    if params=='cluster':
        for i in label_pred:
            plt.plot([data[j][0]], [data[j][1]], mark[i], markersize=5)
            plt.text(data[j][0] + 2, data[j][1], rev_dict[list_of_states[j]], fontsize=8, )
            j += 1
        plt.title('Clustering States Based on Salary and Cost of Living')


    plt.grid(True, lw=2, ls='--', c='.75')
    plt.ylabel('Salary Per in Year USD')
    plt.xlabel('COST OF LIVING in Index (100 as Benchmark)')

    #Beautifying
    ax=plt.subplot(111)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    plt.savefig('ClustersByRegion.png',bbox_inches='tight')
    plt.show()

if __name__=='__main__':
    cluster_region()