import domain
from linguistic_classifier import DGAClassifier
import pandas as pd

lable = ['gameover', 'locky', 'nymaim', 'symmi', 'conficker','pykspa_v2_real', 'pykspa_v2_fake', 'bamital', 'madmax', 'qadars','necurs', 'cryptolocker', 'proslikefan', 'ranbyus', 'murofet',
'suppobox', 'mirai', 'vidro', 'tofsee', 'dyre', 'chinad', 'virut','emotet', 'matsnu', 'blackhole', 'padcrypt', 'xshellghost','ccleaner', 'fobber_v1', 'dircrypt', 'tinba', 'ramnit', 'banjori','simda', 'fobber_v2', 'tempedreve', 'vawtrak', 'rovnix', 'gspy','pykspa_v1', 'shifu']

f1 = open('test123.txt','w+')

df = pd.read_csv('dga1.txt',sep=r'\t',engine='python',header=None)
df.columns = ['a','b','c','d']
count4 = 0

for a in lable:
    count1 = 0
    count2 = 0
    count3 = 0
    for i in range(df.shape[0]):
        str1 = df.ix[i]['a']
        str2 = df.ix[i]['b']
	if  a == str1 :
		        
            count1 +=1

	    try:
	        do = domain.Domain(str2,'False')
            except:
                count4 +=1
	   
            DGA_classifier = DGAClassifier(do)
	    distance = DGA_classifier.classify()

            count3=count3+distance

	    if distance > 1.9975:
                count2 +=1
	     
	    else:
		pass
	       
		      
        else:
            continue

    average_distance = float(count3)/float(count1)
    print '-------------------now compute the radio----------'
    f1.write(a + " " + str(float(count2)/float(count1))  + " " + str(average_distance) + "\n") 
    print '---------------------------has wroten---------------'

print count4
f1.close()

