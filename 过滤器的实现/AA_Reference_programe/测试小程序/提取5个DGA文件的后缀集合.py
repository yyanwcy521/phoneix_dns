import pandas as pd
import tldextract


list_path = ['conficker.a.txt','conficker.b.txt','conficker.c.txt','torpig.txt','bamital.txt']

set2 = set()
for i in list_path:
    df1 = pd.read_csv(i,engine='python',header=None)
    df1.columns = ['domains']
    for j in range(df1.shape[0]):
        set2.add(tldextract.extract(df1.ix[j]['domains']).suffix)
        print '----------------add one suffix------------'
print set2,
