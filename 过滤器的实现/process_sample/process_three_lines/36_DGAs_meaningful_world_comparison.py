import pandas as pd
import matplotlib.pyplot as plt

df_meaning = pd.read_csv('fliter_lt10_Meaningful_str_ratio_statistic.txt',sep=r',',engine='python')

list_type = list(df_meaning['type'])

list_max = list(df_meaning['max_ratio']) 
list_min = list(df_meaning['min_ratio']) 
list_ave = list(df_meaning['average_ratio'])


length = range(len(list_type))

plt.figure(figsize=(15,6))
plt.plot(length,list_max,label="max rate")
plt.plot(length,list_min,label='min rate')
plt.plot(length,list_ave,label='ave rate')

plt.xticks(length,list(list_type),rotation=60,fontsize=12)
plt.yticks(fontsize=12)

plt.xlabel('DGA type',fontsize=18)
plt.ylabel('Meaning World Rate',fontsize=18)
plt.title('36 DGAs meaningful world comparison(max.min.average)',fontsize=25)


plt.legend(loc='best')
plt.show()
