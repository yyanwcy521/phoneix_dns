import domain
from linguistic_classifier import DGAClassifier
import pandas as pd

label = ['gameover', 'locky', 'nymaim', 'symmi', 'conficker','pykspa_v2_real', 'pykspa_v2_fake', 'bamital', 'madmax', 'qadars','necurs', 'cryptolocker', 'proslikefan', 'ranbyus', 'murofet',
'suppobox', 'mirai', 'vidro', 'tofsee', 'dyre', 'chinad', 'virut','emotet', 'matsnu', 'blackhole', 'padcrypt', 'xshellghost','ccleaner', 'fobber_v1', 'dircrypt', 'tinba', 'ramnit', 'banjori','simda', 'fobber_v2', 'tempedreve', 'vawtrak', 'rovnix', 'gspy','pykspa_v1', 'shifu']

f1 = open('aa_alexa_dga1M_statistic.txt','w+')

df = pd.read_csv('dga1.txt',sep=r'\t',engine='python',header=None)
df.columns = ['type','domains','time1','time2']

counter = 0
count4 = 0
dic1 = {}
dic2 = {}

for i in range(df.shape[0]):

    counter += 1

    str1 = df.ix[i]['type']
    str2 = df.ix[i]['domains']

    if str1 in dic1:
        pass
    else:
        dic1[str1] = {}

    if str1 in dic2:
        dic2[str1] += 1
    else:
        dic2[str1] = 1 #dic2 store the per type count.



    try:
	do = domain.Domain(str2,'False')
    except:
	count4 += 1
   
    DGA_classifier = DGAClassifier(do)
    distance = DGA_classifier.classify()

    if dic1[str1].has_key('total_distance'):
        dic1[str1]['total_distance'] += distance
    else:
        dic1[str1]['total_distance'] = distance

   

    if distance < 1.99:
        if dic1[str1].has_key('non_dga_count'):
            dic1[str1]['non_dga_count'] += 1
        else:
	    dic1[str1]['non_dga_count']  = 1
     
 
    if distance < 1.99 and distance > 1.3588:
        if dic1[str1].has_key('recall_count'):
            dic1[str1]['recall_count'] += 1
        else:
            dic1[str1]['recall_count']  = 1

    print '-------------------------------------the counter is %d' %(counter)

for i in label:
    try:
        f1.write(i + "\t" + str(dic2[i])  + "\t" + str(float(dic1[i]['total_distance'])/float(dic2[i])) + "\t" \
                 + str(float(dic1[i]['non_dga_count'])/float(dic2[i])) + "\t" + str(float(dic1[i]['recall_count'])/float(dic1[i]['non_dga_count'])) + "\n") 
    except:
        continue

print count4
f1.close()

