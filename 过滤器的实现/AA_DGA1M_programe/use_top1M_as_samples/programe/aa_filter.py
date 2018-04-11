import pandas as pd
from linguistic_classifier import DGAClassifier
from publicsuffix import  PublicSuffixList
import domain


df = pd.read_csv('dga1.txt',sep=r'\t',engine='python',header=None)
df.columns = ['type','domain','time1','time2']

DGAs = list()
non_DGAs = list()
count = 0
dic_DGA = {}
dic_non_DGA = {}



for do in df['domain']:  
    try:
        print '**********now initialize*********',do
        do = domain.Domain(do,'False')
    except:
        count +=1
        print '--------------------------------------------------------',  
    else:
        DGA_classifier = DGAClassifier(do)
        DGA_classifier.classify(strict = True)
        if do.get_linguistic_feature_set().get_DGA_label() == 'DGA':
            print do,'**********is the DGA domain*************'
            DGAs.append(do)      
        elif do.get_linguistic_feature_set().get_DGA_label() == 'non-DGA':
            print do,'*************************************failed judge'
            non_DGAs.append(do)
        else:
            continue

dic_DGA = {'DGA_domains':DGAs}
dic_non_DGA = {'non_DGA':non_DGAs}
a1 = pd.DataFrame(dic_DGA)
a2 = pd.DataFrame(dic_non_DGA)
a1.to_csv('DGAs.csv')
a2.to_csv('non_DGAs.csv')

print df.shape[0],len(DGAs),len(non_DGAs),count

