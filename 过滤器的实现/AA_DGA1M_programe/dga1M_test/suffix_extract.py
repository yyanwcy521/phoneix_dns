import pandas as pd
import tldextract
df = pd.read_csv('dga1.txt',sep = r'\t',engine='python',header=None)
df.columns = ['a','b','c','d']
s=set()
for i in range(df.shape[0]):
    s.add(tldextract.extract(df.ix[i]['b']).suffix)
print s
