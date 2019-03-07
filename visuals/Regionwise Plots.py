import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import operator

data = pd.read_csv('../data/data_analysis.tsv',sep='\t')    # Supply the file name (path)
data = data.rename(columns = {"COST OF LIVING": "COL", 
                     "ADJUSTED INCOME":"NORM"}) 

#****************************************************************************************************

#Ploting the region tax graphs

tax_data_west = data[data.REGION=='West']
tax_west = sum(tax_data_west.TAX)/tax_data_west.shape[0]
tax_data_south = data[data.REGION=='South']
tax_south = sum(tax_data_south.TAX)/tax_data_south.shape[0]
tax_data_northeast = data[data.REGION=='Northeast']
tax_northeast = sum(tax_data_northeast.TAX)/tax_data_northeast.shape[0]
tax_data_midwest = data[data.REGION=='Midwest']
tax_midwest = sum(tax_data_midwest.TAX)/tax_data_midwest.shape[0]

#Plotting the bar graph

left = [1, 2, 3, 4]   
height = [tax_west, tax_south, tax_northeast, tax_midwest] 
tick_label = ['West', 'South', 'Northeast', 'Midwest'] 
barlist = plt.bar(left, height, tick_label = tick_label, width = 0.4) 
barlist[0].set_color('r')
barlist[1].set_color('y')
barlist[2].set_color('b')
barlist[3].set_color('g')
plt.xlabel('Regions') 
plt.ylabel('Average Tax Rate') 
plt.title('Region wise - Average Tax Rates') 
plt.savefig('Average Tax Rates.png') 

#****************************************************************************************************

#Ploting the region cost of living graphs

col_data_west = data[data.REGION=='West']
col_west = sum(col_data_west.COL)/col_data_west.shape[0]
col_data_south = data[data.REGION=='South']
col_south = sum(col_data_south.COL)/col_data_south.shape[0]
col_data_northeast = data[data.REGION=='Northeast']
col_northeast = sum(col_data_northeast.COL)/col_data_northeast.shape[0]
col_data_midwest = data[data.REGION=='Midwest']
col_midwest = sum(col_data_midwest.COL)/col_data_midwest.shape[0]

#Plotting the bar graph

left = [1, 2, 3, 4]   
height = [col_west, col_south, col_northeast, col_midwest] 
tick_label = ['West', 'South', 'Northeast', 'Midwest'] 
barlist = plt.bar(left, height, tick_label = tick_label, width = 0.4) 
barlist[0].set_color('r')
barlist[1].set_color('y')
barlist[2].set_color('b')
barlist[3].set_color('g')
plt.xlabel('Regions') 
plt.ylabel('Average Cost of Living') 
plt.title('Region wise - Average Cost of Living') 
plt.savefig('Average Cost of Living.png') 

#****************************************************************************************************

#Ploting the region average salaries graphs

sal_data_west = data[data.REGION=='West']
sal_west = sum(sal_data_west.SALARY)/sal_data_west.shape[0]
sal_data_south = data[data.REGION=='South']
sal_south = sum(sal_data_south.SALARY)/sal_data_south.shape[0]
sal_data_northeast = data[data.REGION=='Northeast']
sal_northeast = sum(sal_data_northeast.SALARY)/sal_data_northeast.shape[0]
sal_data_midwest = data[data.REGION=='Midwest']
sal_midwest = sum(sal_data_midwest.SALARY)/sal_data_midwest.shape[0]

#Plotting the bar graph

left = [1, 2, 3, 4]   
height = [sal_west, sal_south, sal_northeast, sal_midwest] 
tick_label = ['West', 'South', 'Northeast', 'Midwest'] 
barlist = plt.bar(left, height, tick_label = tick_label, width = 0.4) 
barlist[0].set_color('r')
barlist[1].set_color('y')
barlist[2].set_color('b')
barlist[3].set_color('g')
plt.xlabel('Regions') 
plt.ylabel('Average Salaries') 
plt.title('Region wise - Average Salaries') 
plt.savefig('Average Salaries.png') 

#****************************************************************************************************

#Ploting the region norm graphs

norm_data_west = data[data.REGION=='West']
norm_west = sum(norm_data_west.NORM)/norm_data_west.shape[0]
norm_data_south = data[data.REGION=='South']
norm_south = sum(norm_data_south.NORM)/norm_data_south.shape[0]
norm_data_northeast = data[data.REGION=='Northeast']
norm_northeast = sum(norm_data_northeast.NORM)/norm_data_northeast.shape[0]
norm_data_midwest = data[data.REGION=='Midwest']
norm_midwest = sum(norm_data_midwest.NORM)/norm_data_midwest.shape[0]

#Plotting the bar graph

left = [1, 2, 3, 4]   
height = [norm_west, norm_south, norm_northeast, norm_midwest] 
tick_label = ['West', 'South', 'Northeast', 'Midwest'] 
barlist = plt.bar(left, height, tick_label = tick_label, width = 0.4) 
barlist[0].set_color('r')
barlist[1].set_color('y')
barlist[2].set_color('b')
barlist[3].set_color('g')
plt.xlabel('Regions') 
plt.ylabel('Normalized Salaries') 
plt.title('Region wise - Normalized Salaries') 
plt.savefig('Normalized Salaries.png') 