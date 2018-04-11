from linguistic_features_extractors import MeaningfulWordsExtractor
import domain
import pandas as pd

dic1 = {}
list_error_domain = []
set1 = set()
counter = 0

f1 = open('Meaningful_str_ratio_statistic.txt','w+')
f1.write('type' + '\t' + 'max_ratio' + '\t' + 'min_ratio' + '\t' + 'average_ratio' + '\n')

df = pd.read_csv('dga1.txt',sep=r'\t',engine='python',header=None)
df.columns = ['type','domains','time1','time2']

for i in range(df.shape[0]):

    str1 = df.ix[i]['type']
    str2 = df.ix[i]['domains']
    try:
	do = domain.Domain(str2,False)
    except:
    	list_error_domain.append(str2)
        continue

		 
    if dic1.has_key(str1):
	dic1[str1].append(MeaningfulWordsExtractor(do).meaningful_words_ratio())
    else:
	dic1[str1] = []
	dic1[str1].append(MeaningfulWordsExtractor(do).meaningful_words_ratio())

    set1.add(str1)
    counter +=1
    print '-'*20, counter

for i in set1:
    max_ratio = max(dic1[i])
    min_ratio = min(dic1[i])
    average_ratio = sum(dic1[i])/float(len(dic1[i]))
    f1.write(i + '\t' + str(max_ratio) + '\t' +  str(min_ratio) + '\t' + str(average_ratio) + '\n' )

f1.close()
print list_error_domain,
