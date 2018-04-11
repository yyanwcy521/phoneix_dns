import statsmodels.api as sm # recommended import according to the docs
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

list_AL = []
list_CA = []
list_CB = []
list_CC = []
list_TO = []
list_BA = []
list_total = [list_AL,list_CA,list_CB,list_CC,list_TO,list_BA]

list_path = ['alexa100_mashi_distance.csv','ConfickerA.txt','ConfickerB.txt','ConfickerC.txt','Torpig.txt','Bamital.txt']

count = 0
for i in list_path:
    df = pd.read_csv(i,engine='python',sep=' ',header=None)
    df.columns = ['domains','distance']
    for j in range(df.shape[0]):
        list_total[count].append(df.ix[j]['distance'])
    count += 1
print 'The  alexa100  length is',len(list_AL),'\n'
print 'The ConfickerA length is',len(list_CA),'\n'
print 'The ConfickerB length is',len(list_CB),'\n'
print 'The ConfickerC length is',len(list_CC),'\n'
print 'The    Torpig  length is',len(list_TO),'\n'
print 'The    Bamital length is',len(list_BA),'\n'

ecdf_AL = sm.distributions.ECDF(list_AL)
ecdf_CA = sm.distributions.ECDF(list_CA)
ecdf_CB = sm.distributions.ECDF(list_CB)
ecdf_CC = sm.distributions.ECDF(list_CC)
ecdf_TO = sm.distributions.ECDF(list_TO)
ecdf_BA = sm.distributions.ECDF(list_BA)

x_AL = np.linspace(min(list_AL), max(list_AL))
x_CA = np.linspace(min(list_CA), max(list_CA))
x_CB = np.linspace(min(list_CB), max(list_CB))
x_CC = np.linspace(min(list_CC), max(list_CC))
x_TO = np.linspace(min(list_TO), max(list_TO))
x_BA = np.linspace(min(list_BA), max(list_BA))

y_AL = ecdf_AL(x_AL)
y_CA = ecdf_CA(x_CA)
y_CB = ecdf_CB(x_CB)
y_CC = ecdf_CC(x_CC)
y_TO = ecdf_TO(x_TO)
y_BA = ecdf_BA(x_BA)


plt.figure(figsize=(8,8))
plt.plot(x_AL, y_AL,label = 'Alexa10')
plt.plot(x_CA, y_CA,label = 'ConfickerA')
plt.plot(x_CB, y_CB,label = 'ConfickerB')
plt.plot(x_CC, y_CC,label = 'ConfickerC')
plt.plot(x_TO, y_TO,label = 'Torpig')
plt.plot(x_BA, y_BA,label = 'Bamital')
plt.legend(loc = 'upper left')
plt.show()


