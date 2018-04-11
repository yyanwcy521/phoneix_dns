import pandas as pd
import matplotlib.pyplot as plt

df_alexa = pd.read_csv('aa_filter_lt10_alexa_dga1M_statistic.csv',sep=r',',engine='python')
df_top1M = pd.read_csv('fliter_lt10_dga1M_statistics.csv',sep=r',',engine='python')

list_type = list(df_alexa['type'])
list_alexa_distance = list(df_alexa['average_distance']) 
list_top1M_distance = list(df_top1M['average_distance'])

length = len(list_alexa_distance)

plt.figure(figsize=(15,6))
plt.plot(length,list_alexa_distance,label="Alexa10W")
plt.plot(length,list_top1M_distance,label='TOP1M')

plt.xticks(length,list(list_type),rotation=60,fontsize=12)
plt.yticks(fontsize=12)

plt.xlabel('DGA type',fontsize=18)
plt.ylabel('average mahalanobis distance',fontsize=18)
plt.title('average mahalanobis distance  comparison',fontsize=25)


plt.legend(loc='upper left')
plt.show()  
